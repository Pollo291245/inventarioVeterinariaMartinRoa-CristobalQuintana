from django.shortcuts import render
from django.views.generic import CreateView
from django.shortcuts import redirect
from gestorProductos.models import Categoria, Producto
from gestorProductos.forms import ProductoForm, CategoriaForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def citasView(request):
    return render(request, 'gestorProductos/citas.html')

def serviciosView(request):
    productos = Producto.objects.all()[0:3]
    return render(request, 'gestorProductos/servicios.html', {'productos': productos})

def categoriasView(request):
    categorias=Categoria.objects.all()
    return render(request, 'gestorProductos/categorias.html', {'categorias': categorias})

def editar_categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'gestorProductos/editar_categoria.html', {'form': form})

def eliminar_categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    categoria.delete()
    return redirect('categorias')



def ProductosView(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()

    if request.GET.get('categoria'):
        categoria_id = request.GET.get('categoria')
        if categoria_id != "":
            productos = productos.filter(categoria_id=categoria_id)

    if request.GET.get('search'):
        search_query = request.GET.get('search')
        productos = productos.filter(nombre__icontains=search_query)

    return render(request, 'gestorProductos/productos.html', {'categorias': categorias, 'productos': productos})


def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = CategoriaForm()
    return render(request, 'gestorProductos/agregar_categoria.html', {'form': form})


@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.created_by = request.user
            producto.save()
            return redirect('productos')
    else:
        form = ProductoForm()
    
    data={'form':form,'categorias':Categoria.objects.all()}
    return render(request, 'gestorProductos/agregar_producto.html', data)

def editar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'gestorProductos/editar_producto.html', {'form': form})

def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.delete()
    return redirect('productos')



