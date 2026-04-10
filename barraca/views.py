from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required # Importamos el decorador de seguridad
from .models import Producto, Post, Proveedor 
from .forms import ProductoForm, ProveedorForm, PedidoForm

# --- VISTAS GENERALES ---

def inicio(request):
    return render(request, "barraca/inicio.html")

def about(request):
    return render(request, "barraca/about.html")

# --- VISTAS DEL BLOG (ENTREGA FINAL) ---

def listar_posts(request):
    posts = Post.objects.all().order_by('-fecha')
    return render(request, "barraca/listar_posts.html", {"posts": posts})

def detalle_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "barraca/detalle_post.html", {"post": post})

# --- VISTAS BASADAS EN CLASES (CBV) PARA POSTS ---

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "barraca/post_form.html"
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
    success_url = reverse_lazy('listar_posts')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "barraca/post_form.html"
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
    success_url = reverse_lazy('listar_posts')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "barraca/post_confirm_delete.html"
    success_url = reverse_lazy('listar_posts')

# --- VISTAS DE GESTIÓN (FERRETERÍA) ---

@login_required
def formulario_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request, "barraca/inicio.html", {"mensaje": "Producto guardado con éxito"})
            except Exception as e:
                return render(request, "barraca/inicio.html", {"mensaje": f"Error fatal: {e}"})
    else:
        form = ProductoForm()
    return render(request, "barraca/form_generico.html", {"form": form, "titulo": "Cargar Producto"})

@login_required
def formulario_proveedor(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request, "barraca/inicio.html", {"mensaje": "Proveedor guardado con éxito"})
            except Exception as e:
                return render(request, "barraca/inicio.html", {"mensaje": f"Error al guardar: {e}"})
    else:
        form = ProveedorForm()
    return render(request, "barraca/form_generico.html", {"form": form, "titulo": "Nuevo Proveedor"})

# --- GESTIÓN DE PRODUCTOS (LISTADO UNIFICADO CON BÚSQUEDA Y BORRADO) ---

def listar_productos(request):
    nombre_a_buscar = request.GET.get('nombre', '')
    if nombre_a_buscar:
        productos = Producto.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        productos = Producto.objects.all()
        
    return render(request, "barraca/listar_productos.html", {
        "productos": productos, 
        "query": nombre_a_buscar
    })

@login_required # Solo usuarios logueados pueden borrar
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    
    productos = Producto.objects.all()
    return render(request, "barraca/listar_productos.html", {
        "productos": productos, 
        "mensaje": f"Producto '{producto.nombre}' eliminado correctamente."
    })

# --- GESTIÓN DE PROVEEDORES ---

def listar_proveedores(request):
    nombre_a_buscar = request.GET.get('nombre', '')
    if nombre_a_buscar:
        proveedores = Proveedor.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        proveedores = Proveedor.objects.all()
        
    return render(request, "barraca/listar_proveedores.html", {
        "proveedores": proveedores, 
        "query": nombre_a_buscar
    })

@login_required 
def eliminar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    proveedor.delete()
    return redirect("listar_proveedores")



def buscar_producto(request):
    return render(request, "barraca/buscar.html")

def resultados_busqueda(request):
    if "nombre" in request.GET:
        nombre = request.GET["nombre"]
        productos = Producto.objects.filter(nombre__icontains=nombre)
        return render(request, "barraca/resultados.html", {"productos": productos, "query": nombre})
    
    return render(request, "barraca/inicio.html", {"mensaje": "No enviaste datos para buscar"})
