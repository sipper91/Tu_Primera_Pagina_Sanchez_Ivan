from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField # Importante: requiere instalar django-ckeditor



class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=11)
    rubro = models.CharField(max_length=50) 

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    fecha = models.DateField()
    descripcion = models.TextField()
    entregado = models.BooleanField(default=False)

    def __str__(self):
        return f"Pedido del {self.fecha} - Entregado: {self.entregado}"




class Post(models.Model):
    
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    
    
    cuerpo = RichTextField() 
    
    
    imagen = models.ImageField(upload_to='pages', null=True, blank=True)
    
    
    fecha = models.DateField(auto_now_add=True)
    
    
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} | por {self.autor}"
