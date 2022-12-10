from django.contrib import admin

# Register your models here.
from apps.room.models import Room

class RoomAdmin(admin.ModelAdmin):
	list_display = ('id','code','name')

admin.site.register(Room, RoomAdmin)