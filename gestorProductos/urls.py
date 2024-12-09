from django.urls import path
from gestorProductos.views import ProductosView, citasView, serviciosView,agregar_producto,agregar_categoria,editar_producto,eliminar_producto,categoriasView,editar_categoria,eliminar_categoria


urlpatterns = [
    path('productos/', ProductosView,name='productos'),
    path ('citas/', citasView,name='citas'),
    path('servicios/', serviciosView,name='servicios'),
    path('agregar_producto/', agregar_producto,name='agregar_producto'),
    path('agregar_categoria/', agregar_categoria,name='agregar_categoria'),
    path('editar_producto/<int:producto_id>', editar_producto,name='editar_producto'),
    path('eliminar_producto/<int:producto_id>', eliminar_producto,name='eliminar_producto'),
    path('categorias/', categoriasView,name='categorias'),
    path('editar_categoria/<int:categoria_id>', editar_categoria,name='editar_categoria'),
    path('eliminar_categoria/<int:categoria_id>', eliminar_categoria,name='eliminar_categoria'),
]