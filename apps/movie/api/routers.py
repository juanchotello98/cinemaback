from rest_framework.routers import DefaultRouter
from apps.movie.api.views.viewsets import MovieViewSet

router = DefaultRouter()

router.register(r'movies', MovieViewSet, basename = 'movies')

urlpatterns = router.urls