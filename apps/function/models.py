from django.db import models
from apps.movie.models import Movie
from apps.room.models import Room

# Create your models here.

class Function(models.Model):
	id = models.AutoField(primary_key = True)
	code = models.CharField("codigo de funcion", max_length = 125, unique = True)
	movie = models.ForeignKey(Movie, on_delete = models.CASCADE, verbose_name = 'pelicula')
	room  = models.ForeignKey(Room, on_delete = models.CASCADE, verbose_name = 'sala')
	date = models.DateField(verbose_name = 'fecha')
	time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name = 'hora')

	class Meta:
		verbose_name = 'funcion'
		verbose_name_plural = 'funciones'

	def __str__(self):
		return f'{self.code}'