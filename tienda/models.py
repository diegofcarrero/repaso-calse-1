from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def _str_(self):
        return f'{self.nombre} - (${self.precio})'

class Cliente(models.Model):
    nombre = models.CharField(max_length=120)
    correo = models.EmailField(unique=True)
    fecha_registro = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def _str_(self):
        return f'{self.nombre} <{self.correo}>'
    
class Pedido(models.Model):
    ESTADOS = [
        ('CREADO', 'Creado'),
        ('PAGADO', 'Pagado'),
        ('ENVIADO', 'Enviado'),
        ('CERRADO', 'Cerrado'),
    ]
    estado = models.CharField(max_length=120, choices=ESTADOS, default='CREADO')
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    productos = models.ManyToManyField(Producto, related_name='pedidos')

    def _str_(self):
        return f'Pedido #{self.pk} - {self.cliente.nombre} - ({self.estado})'