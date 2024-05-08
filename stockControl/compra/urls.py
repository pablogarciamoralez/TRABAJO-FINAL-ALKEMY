from django.urls import path
from .views import (home, crearProducto, crearProveedor)

urlpatterns = [
    path('', home, name='home'),
    path('crearproducto/', crearProducto, name='crearproducto'),
    path('crearproveedor/', crearProveedor, name='crearproveedor'),
]