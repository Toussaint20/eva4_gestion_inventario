from django.urls import path
from . import views
from .views import login_view, home_view, crud_categoria, crud_proveedor, crud_producto, editar_proveedor, eliminar_proveedor

urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('categorias/', views.crud_categoria, name='crud_categoria'),
    path('categoria/nuevo/', views.crear_categoria, name='crear_categoria'),
    path('categoria/editar/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),
    path('categoria/<int:id>/', views.eliminar_categoria, name='eliminar_categoria'),
    path('proveedores/', views.crud_proveedor, name='crud_proveedor'),
    path('proveedor/nuevo/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedor/editar/<int:proveedor_id>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedor/eliminar/<int:id>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('productos/', views.crud_producto, name='crud_producto'),
    path('producto/nuevo/', views.crear_producto, name='crear_producto'),
    path('producto/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('producto/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
]
