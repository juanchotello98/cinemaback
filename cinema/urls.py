
from django.contrib import admin
from django.urls import path, include
from apps.users.views import Login, Logout, UserToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name = 'login'),
    path('logout/', Logout.as_view(), name = 'logout'),
    path('refresh-token/', UserToken.as_view(), name = 'refresh_token'),
    path('user/',include('apps.users.api.routers')),
    path('room/', include('apps.room.api.routers')),
    path('movie/', include('apps.movie.api.routers')),
    path('function/', include('apps.function.api.routers'))
]