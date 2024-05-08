from django.contrib import admin
from .models import Producto, Proveedor

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'proveedor',]


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'dni']


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
# Register your models here.
