from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from garagem.views import MarcaViewSet


router = routers.DefaultRouter()
router.register(r"marcas", MarcaViewSet)

urlpatterns = [path("admin/", admin.site.urls), path("", include(router.urls))]