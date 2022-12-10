from django.db import models

# Create your models here.

class Movie(models.Model):

	CLASSIFICATIONS = [
	('TP', 'TP'),
	('7', '7'),
	('12', '12'),
	('15', '15'),
	('18', '18')
	]

	id = models.AutoField(primary_key = True)
	name = models.CharField("nombre de pelicula", max_length = 125)
	code = models.CharField("codigo de pelicula", max_length = 125, unique = True)
	classification = models.CharField("clasificacion", max_length = 125,choices = CLASSIFICATIONS,  default = 'sin clasificacion')

	class Meta:
		verbose_name = 'pelicula'
		verbose_name_plural = 'peliculas'

	def __str__(self):
		return f'{self.name}'