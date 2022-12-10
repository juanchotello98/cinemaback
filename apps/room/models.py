from django.db import models

# Create your models here.

class Room(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField("nombre de sala", max_length = 125)
	code = models.CharField("codigo de sala", max_length = 125, unique = True)
	capacity = models.IntegerField("capacidad")

	class Meta:
		verbose_name = 'sala'
		verbose_name_plural = 'salas'

	def __str__(self):
		return f'{self.name}'