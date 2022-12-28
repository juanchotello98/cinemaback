from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from apps.room.models import Room
from apps.function.models import Function
from apps.room.api.serializers.serializers import RoomSerializer
from apps.users.authentication_mixins import Authentication


class RoomViewSet(Authentication,viewsets.ModelViewSet):
	serializer_class = RoomSerializer

	def get_queryset(self, pk = None):
		if pk is None:
			return Room.objects.all()
		return Room.objects.filter(id = pk).first()


	def list(self, request):
		rooms = self.get_queryset()
		room_serializer = self.get_serializer(rooms, many = True)
		return Response(room_serializer.data, status = status.HTTP_200_OK)


	def create(self, request):
		room_serializer = self.get_serializer(data = request.data)
		if room_serializer.is_valid():
			room_serializer.save()
			return Response({'message': 'Sala creada exitosamente'}, status = status.HTTP_201_CREATED)
		return Response(room_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


	def retrieve(self, request, pk = None):
		room = self.get_queryset(pk)
		if room:
			room_serializer = self.get_serializer(room)
			return Response(room_serializer.data, status = status.HTTP_200_OK)
		return Response({'error':'No se ha encontrado una sala con estos datos'}, status = status.HTTP_400_BAD_REQUEST)


	def partial_update(self, request, pk = None):
		room = self.get_queryset(pk)
		if room:
			room_serializer = self.get_serializer(room)
			return Response(room_serializer.data, status = status.HTTP_200_OK)
		return Response({'error':'No se ha encontrado una sala con estos datos'}, status = status.HTTP_400_BAD_REQUEST)


	def update(self, request, pk = None):
		room = self.get_queryset(pk)
		if room:
			room_serializer = self.get_serializer(room, data = request.data)
			if room_serializer.is_valid():
				room_serializer.save()
				return Response({'message':'Sala actualizada exitosamente', 'data':room_serializer.data}, status = status.HTTP_200_OK)
			return Response({'error':'No se ha encontrado una sala con estos datos'}, status = status.HTTP_400_BAD_REQUEST) 


	def destroy(self, request, pk = None):
		room = self.get_queryset(pk)

		room_in_function = Function.objects.filter(room = pk).exists()

		if room_in_function:
			return Response({'error': 'No puede eliminar una sala que esté asociada a una función'}, status = status.HTTP_405_METHOD_NOT_ALLOWED)
		elif room: 
			room.delete()
			return Response({'message':'Sala eliminada exitosamente'}, status = status.HTTP_204_NO_CONTENT)
		return Response({'error':'No se ha encontrado una sala con estos datos'}, status = status.HTTP_400_BAD_REQUEST)