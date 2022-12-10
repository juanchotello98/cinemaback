from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from apps.function.models import Function
from apps.movie.models import Movie
from apps.room.models import Room
from apps.function.api.serializers.serializers import FunctionSerializer


class FunctionViewSet(viewsets.ModelViewSet):
	serializer_class = FunctionSerializer

	def get_queryset(self, pk = None):
		if pk is None:
			return Function.objects.all()
		return Function.objects.filter(id = pk).first()


	def list(self, request):
		functions = self.get_queryset()
		function_serializer = self.get_serializer(functions, many = True)
		return Response(function_serializer.data, status = status.HTTP_200_OK)


	def create(self, request): 
		function_serializer = self.get_serializer(data = request.data)
		
		id_movie = request.data['movie']
		movie = Movie.objects.filter(id=id_movie).exists()

		id_room = request.data['room']
		room = Room.objects.filter(id=id_room).exists()

		if not movie and not room:
			return Response({'error':'No puede crear una funcion con una pelicula y sala inexistente'}, status = status.HTTP_405_METHOD_NOT_ALLOWED)

		if not movie:	
			return Response({'error':'No puede crear una funcion con una pelicula inexistente'}, status = status.HTTP_405_METHOD_NOT_ALLOWED)

		if not room:	
			return Response({'error':'No puede crear una funcion con una sala inexistente'}, status = status.HTTP_405_METHOD_NOT_ALLOWED)

		if function_serializer.is_valid():
			function_serializer.save()
			return Response({'message':'Funcion creada exitosamente'}, status = status.HTTP_201_CREATED)
		return Response(function_serializer.errors,status = status.HTTP_400_BAD_REQUEST)


	def retrieve(self, request, pk = None): 
		function = self.get_queryset(pk)
		if function:
			function_serializer =  self.get_serializer(function)
			return Response(function_serializer.data, status = status.HTTP_200_OK)
		return Response({'error':'No se ha encontrado una funcion con estos datos'}, status = status.HTTP_400_BAD_REQUEST)


	def partial_update(self, request, pk = None):
		function = self.get_queryset(pk)
		if function:
			function_serializer = self.get_serializer(function)
			return Response(function_serializer.data, status = status.HTTP_200_OK)
		return Response({'error':'No se ha encontrado una funcion con estos datos'}, status = status.HTTP_400_BAD_REQUEST)


	def update(self, request, pk = None):
		function = self.get_queryset(pk)
		if function:
			function_serializer = self.get_serializer(function, data = request.data)
			if function_serializer.is_valid():
				function_serializer.save()
				return Response({'message':'Funcion actualizada exitosamente','data':function_serializer.data}, status = status.HTTP_200_OK)
			return Response({'error':'No se ha encontrado una funcion con estos datos'}, status = status.HTTP_400_BAD_REQUEST)


	def destroy(self, request, pk = None): 
		function = self.get_queryset(pk)
		if function:
			function.delete()
			return Response({'message':'funcion eliminada exitosamente'}, status = status.HTTP_204_NO_CONTENT)
		return Response({'error':'No se ha encontrado una funcion con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
