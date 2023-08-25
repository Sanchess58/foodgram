from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("api/swagger/", SpectacularAPIView.as_view()),
    path("api/docs/", SpectacularSwaggerView.as_view())
]
