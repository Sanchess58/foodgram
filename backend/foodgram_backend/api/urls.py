from django.urls import path, include
from .views import ReceiptViewSet
app_name = "api"

urlpatterns = [
    path("api/recipes/", ReceiptViewSet.as_view(), name="recipes")
]
