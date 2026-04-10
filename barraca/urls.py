from django.urls import path
from .views import (
    inicio, 
    about, 
    listar_posts, 
    detalle_post, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView,
    formulario_producto, 
    formulario_proveedor, 
    buscar_producto, 
    listar_productos, 
    eliminar_producto,
    listar_proveedores, 
    eliminar_proveedor,
    resultados_busqueda
)

urlpatterns = [
    
    path('', inicio, name='inicio'),
    path('about/', about, name='about'),
    
    
    path('blog/', listar_posts, name='listar_posts'),
    path('blog/<int:id>/', detalle_post, name='detalle_post'),
    path('blog/create/', PostCreateView.as_view(), name='post_create'),
    path('blog/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('blog/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),


    
    path('form_producto/', formulario_producto, name='form_producto'),
    path('form_proveedor/', formulario_proveedor, name='form_proveedor'),
    path('buscar/', buscar_producto, name='buscar'),
    path('resultados/', resultados_busqueda, name='resultados_busqueda'),
    path('productos/lista/', listar_productos, name='listar_productos'),
    path('productos/eliminar/<int:id>/', eliminar_producto, name='eliminar_producto'),
    path('proveedores/lista/', listar_proveedores, name='listar_proveedores'),
    path('proveedores/eliminar/<int:id>/', eliminar_proveedor, name='eliminar_proveedor'),

]
