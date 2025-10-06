from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-creado_en',)

    def __str__(self):
        return f"{self.nombre} | {self.precio}"