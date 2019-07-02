from django.contrib import admin
from .models import User, Cliente, Proveedor, Plato, Orden_compra, Empleado, Orden_pedido, Producto

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Plato)
admin.site.register(Orden_compra)
admin.site.register(Empleado)
admin.site.register(Orden_pedido)
admin.site.register(Producto)