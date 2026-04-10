from django.contrib import admin
from .models import Producto, Proveedor, Pedido, Post


admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Pedido)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha') 
    search_fields = ('titulo', 'subtitulo')    
