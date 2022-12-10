from django.contrib import admin

# Register your models here.
from apps.function.models import Function

class FunctionAdmin(admin.ModelAdmin):
	list_display = ('id','code','movie', 'room', 'date', 'time')

admin.site.register(Function, FunctionAdmin)