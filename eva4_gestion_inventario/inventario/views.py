from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Categoria, Proveedor, Producto, Cliente, Pedido, PedidoProducto, Factura
from .serializers import CategoriaSerializer, ProveedorSerializer, ProductoSerializer, ClienteSerializer, FacturaSerializer, PedidoSerializer, PedidoProductoSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProveedorViewSet(ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ProductoViewSet(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "¡Acceso autorizado! Solo usuarios autenticados pueden ver esto."})
    
class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PedidoProductoViewSet(ModelViewSet):
    queryset = PedidoProducto.objects.all()
    serializer_class = PedidoProductoSerializer

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class FacturaViewSet(ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    
@api_view(['POST'])
@permission_classes([IsAdminUser])  # Solo administradores pueden registrar usuarios
def register_user(request):
    if request.method == 'POST':
        # Extraer los datos del cuerpo de la solicitud
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        # Crear usuario
        user = User.objects.create_user(username=username, email=email, password=password)

        # Generar token JWT
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({
            'access': access_token,
            'refresh': str(refresh)
        }, status=status.HTTP_201_CREATED)    