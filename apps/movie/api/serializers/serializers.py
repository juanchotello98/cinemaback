from rest_framework import serializers
from apps.movie.models import Movie

class MovieSerializer(serializers.ModelSerializer):

	class Meta:
		model = Movie
		fields = '__all__'