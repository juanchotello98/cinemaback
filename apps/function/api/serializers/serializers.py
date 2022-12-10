from rest_framework import serializers
from apps.function.models import Function
from apps.movie.api.serializers.serializers import MovieSerializer
from apps.room.api.serializers.serializers import RoomSerializer

class FunctionSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Function
		fields = '__all__'


	def to_representation(self, instance):
		return {
			'id': instance.id,
			'code': instance.code,
			'movie': instance.movie.name,
			'room': instance.room.name,
			'date': instance.date.strftime('%Y-%m-%d'),
			'time': instance.time
		}
