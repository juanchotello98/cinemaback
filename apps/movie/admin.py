from django.contrib import admin

# Register your models here.
from apps.movie.models import Movie

class MovieAdmin(admin.ModelAdmin):
	list_display = ('id','code','name')

admin.site.register(Movie,MovieAdmin)