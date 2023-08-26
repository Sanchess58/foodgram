from django.urls import path, include
from .views import ReceiptViewSet
from rest_framework.routers import DefaultRouter
app_name = "api"

router = DefaultRouter()
router.register(r'recipes', ReceiptViewSet, basename='recipres')
urlpatterns = [
    path("", include(router.urls))
]
