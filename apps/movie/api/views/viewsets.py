from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from apps.movie.models import Movie
from apps.function.models import Function
from apps.movie.api.serializers.serializers import MovieSerializer
from apps.users.authentication_mixins import Authentication


class MovieViewSet(Authentication,viewsets.ModelViewSet):
	serializer_class = MovieSerializer

	def get_queryset(self, pk = None):
		if pk is None:
			return Movie.objects.all()
		return Movie.objects.filter(id = pk).first()


	def list(self, request):
		movies = self.get_queryset()
		movie_serializer = self.get_serializer(movies, many = True)
		return Response(movie_serializer.data, status = status.HTTP_200_OK)


	def create(self, request):
		movie_serializer = self.get_serializer(data = request.data)
		if movie_serializer.is_valid():
			movie_serializer.save()
			return  Response({'message': 'Pelicula creada exitosamente'}, status = status.HTTP_201_CREATED)
		return Response(movie_serializer.errors,status = status.HTTP_400_BAD_REQUEST)


	def retrieve(self, request, pk = None):
		movie = self.get_queryset(pk)
		if movie:
			movie_serializer = self.get_serializer(movie)
			return Response(movie_serializer.data, status = status.HTTP_200_OK)
		return Response({'error':'No se ha encontrado una película con estos datos'}, status = status.HTTP_400_BAD_REQUEST)


	def partial_update(self, request, pk = None):
		movie = self.get_queryset(pk)
		if movie:
			movie_serializer = self.get_serializer(movie)
			return Response(movie_serializer.data, status = status.HTTP_200_OK)
		return Response({'error':'No se ha encontrado una película con estos datos'}, status = status.HTTP_400_BAD_REQUEST)


	def update(self, request, pk = None):
		movie = self.get_queryset(pk)
		if movie:
			movie_serializer = self.get_serializer(movie, data = request.data)
			if movie_serializer.is_valid():
				movie_serializer.save()
				return Response({'message':'Pelicula actulizada exitosamente','data':movie_serializer.data}, status = status.HTTP_200_OK)
			return Response({'error': 'No se ha encontrado una película con estos datos'}, status = status.HTTP_400_BAD_REQUEST)


	def destroy(self, request, pk = None):
		movie = self.get_queryset(pk)

		movie_in_function = Function.objects.filter(movie = pk).exists()

		if movie_in_function:
			return Response({'error':'No puede eliminar un película que esté asociada a una función'}, status = status.HTTP_405_METHOD_NOT_ALLOWED)
		elif movie:
			movie.delete()
			return Response({'message':'película eliminada exitosamente'}, status = status.HTTP_204_NO_CONTENT)
		return Response({'error':'No se ha encontrado una película con estos datos'}, status = status.HTTP_400_BAD_REQUEST)