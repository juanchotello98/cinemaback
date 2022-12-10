from rest_framework.routers import DefaultRouter
from apps.room.api.views.viewsets import RoomViewSet

router = DefaultRouter()

router.register(r'rooms', RoomViewSet, basename = 'rooms')

urlpatterns = router.urls