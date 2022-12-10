
from django.contrib import admin
from django.urls import path, include, re_path
from apps.users.views import Login, Logout, RefreshToken
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",
      default_version='v0.1',
      description="Cinema website management public documentation ",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="juandavidtello98@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name = 'login'),
    path('logout/', Logout.as_view(), name = 'logout'),
    path('refresh-token/', RefreshToken.as_view(), name = 'refresh_token'),
    path('user/',include('apps.users.api.routers')),
    path('room/', include('apps.room.api.routers')),
    path('movie/', include('apps.movie.api.routers')),
    path('function/', include('apps.function.api.routers'))
]