from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from garagem.views import MarcaViewSet, CategoriaViewSet, CorViewSet


router = routers.DefaultRouter()
router.register(r"marcas", MarcaViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"cores", CorViewSet)


urlpatterns = [path("admin/", admin.site.urls), path("", include(router.urls))]