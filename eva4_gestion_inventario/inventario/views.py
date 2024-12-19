from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Categoria, Proveedor, Producto, Cliente, Pedido, PedidoProducto
from .serializers import CategoriaSerializer, ProveedorSerializer, ProductoSerializer, ClienteSerializer, PedidoSerializer, PedidoProductoSerializer
from .forms import ProveedorForm, CategoriaForm, ProductoForm

#views a nivel de api
class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProveedorViewSet(ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ProductoViewSet(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PedidoProductoViewSet(ModelViewSet):
    queryset = PedidoProducto.objects.all()
    serializer_class = PedidoProductoSerializer

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    
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

#views de templates html
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')

def home_view(request):
    return render(request, 'home.html')

def crud_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'crud_categoria.html', {'categorias': categorias})

def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_categoria')  # Redirigir a la vista de listado de categorías
    else:
        form = CategoriaForm()
    return render(request, 'crear_categoria.html', {'form': form})

def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('crud_categoria')  # Redirigir a la vista de listado de categorías
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'editar_categoria.html', {'form': form, 'categoria': categoria})

def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    categoria.delete()
    return redirect('crud_categoria')  # Redirigir a la vista de listado de categorías

# Proveedor
def crud_proveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'crud_proveedor.html', {'proveedores': proveedores})

def crear_proveedor(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_proveedor')  # Redirigir a la vista de listado de proveedores
    else:
        form = ProveedorForm()
    return render(request, 'crear_proveedor.html', {'form': form})

def editar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == "POST":
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('crud_proveedor')  # Redirigir a la vista de listado de proveedores
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'editar_proveedor.html', {'form': form, 'proveedor': proveedor})

def eliminar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    proveedor.delete()
    return redirect('crud_proveedor')  # Redirigir a la vista de listado de proveedores

# Producto
def crud_producto(request):
    productos = Producto.objects.all()
    return render(request, 'crud_producto.html', {'productos': productos})

def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_producto')  # Redirigir a la vista de listado de productos
    else:
        form = ProductoForm()
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()
    return render(request, 'crear_producto.html', {'form': form, 'categorias': categorias, 'proveedores': proveedores})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('crud_producto')  # Redirigir a la vista de listado de productos
    else:
        form = ProductoForm(instance=producto)
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto, 'categorias': categorias, 'proveedores': proveedores})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('crud_producto')  # Redirigir a la vista de listado de productos
