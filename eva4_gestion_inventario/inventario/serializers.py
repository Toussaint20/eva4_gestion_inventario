from rest_framework import serializers
from .models import Categoria, Proveedor, Producto, Pedido, Factura, PedidoProducto, Cliente

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class PedidoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoProducto
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    productos = PedidoProductoSerializer(many=True, source='pedidoproducto_set', read_only=True)

    class Meta:
        model = Pedido
        fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'