from django.contrib import admin
from .models import Cliente, Producto, Pedido

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display =("nombre","correo","activo", "fecha_registro")
    search_fields= ("nombre", "correo")
    list_filter =("activo",)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display =("nombre","precio")
    search_fields= ("nombre",)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display =("id","cliente","estado", "fecha")
    search_fields= ("estado", "fecha")
    list_filter =("estado", "fecha")