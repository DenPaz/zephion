from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from apps.sensors.api.views import SensorReadingViewSet
from apps.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("sensor-readings", SensorReadingViewSet)

app_name = "api"
urlpatterns = router.urls
