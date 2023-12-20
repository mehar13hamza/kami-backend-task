from django.urls import path, include
from rest_framework.routers import DefaultRouter
from airplane.views import AirplaneView

router = DefaultRouter()
router.register(r"airplane", AirplaneView, basename="airplane")
urlpatterns = router.urls
