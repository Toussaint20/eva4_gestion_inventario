from django.contrib import admin
from .models import Categoria, Proveedor, Producto, Cliente, Pedido, PedidoProducto

# Registra los modelos
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(PedidoProducto)
