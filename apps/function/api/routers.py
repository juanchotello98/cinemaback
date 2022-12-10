from rest_framework.routers import DefaultRouter
from apps.function.api.views.viewsets import FunctionViewSet

router = DefaultRouter()

router.register(r'functions', FunctionViewSet, basename = 'functions')

urlpatterns = router.urls