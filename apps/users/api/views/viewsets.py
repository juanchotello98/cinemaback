from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from apps.users.models import User
from apps.users.api.serializers.serializers import UserSerializer, UserListSerializer
from apps.users.authentication_mixins import Authentication


class UserViewSet(Authentication,viewsets.ModelViewSet):

	serializers = {
		'default': UserSerializer,
		'list': UserListSerializer
	}

	def get_serializer_class(self):
		return self.serializers.get(self.action, self.serializers['default'])


	def get_queryset(self, pk = None):
		if pk is None:
			return User.objects.all().values('id', 'name', 'username', 'email', 'password')
		return User.objects.filter(id = pk).first()


	def list(self, request):
		users = self.get_queryset()
		user_serializer = self.get_serializer(users, many = True)
		print(self.user)
		return Response(user_serializer.data, status = status.HTTP_200_OK)


	def create(self, request):
		user_serializer = self.get_serializer(data = request.data)
		if user_serializer.is_valid():
			user_serializer.save()
			return Response({'message':'Usuario creado exitosamente'}, status = status.HTTP_201_CREATED)
		return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


	def retrieve(self, request, pk = None):
		user = self.get_queryset(pk)
		if user:
			user_serializer = self.get_serializer(user)
			return Response(user_serializer.data, status = status.HTTP_200_OK)
		return Response({'error':'No se ha encontrado un usuario con estos datos'}, status = status.HTTP_400_BAD_REQUEST)


	def partial_update(self, request, pk = None):
		user = self.get_queryset(pk)
		if user:
			user_serializer = self.get_serializer(user)
			return Response(user_serializer.data, status = status.HTTP_200_OK)
		return Response({'error':'No se ha encontrado un usuario con estos datos'}, status = status.HTTP_400_BAD_REQUEST)


	def update(self, request, pk = None):
		user = self.get_queryset(pk)
		if user:
			user_serializer = self.get_serializer(user, data = request.data)
			if user_serializer.is_valid():
				user_serializer.save()
				return Response({'message':'Usuario actualizado exitosamente','data':user_serializer.data}, status = status.HTTP_200_OK)
			return Response({'error':'No se ha encontrado un usuario con estos datos'}, status = status.HTTP_400_BAD_REQUEST)


	def destroy(self, request, pk = None):
		user = self.get_queryset(pk)
		if user:
			user.delete()
			return Response({'message':'Usuario eliminado exitosamente'}, status = status.HTTP_204_NO_CONTENT)
		return Response({'error':'No se ha encontrado un usuario con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
