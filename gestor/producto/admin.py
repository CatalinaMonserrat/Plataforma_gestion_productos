from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'creado_en')
    list_filter = ('creado_en',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('-creado_en',)

# Solo el superusuario puede eliminar desde el admin:
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
