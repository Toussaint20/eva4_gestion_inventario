from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, ProveedorViewSet, ProductoViewSet, ClienteViewSet, PedidoViewSet, PedidoProductoViewSet, FacturaViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ProtectedView
from . import views

# router para registrar vistas
router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'pedido-productos', PedidoProductoViewSet)
router.register(r'facturas', FacturaViewSet)
#rutas para login JWT
jwt_urls = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    *jwt_urls,  #rutas JWT en la app
] + router.urls
urlpatterns += [
    # Endpoint para registrar usuarios nuevos
    path('register/', views.register_user, name='register_user'),  
    path('api/protected/', ProtectedView.as_view(), name='protected_view'),
]