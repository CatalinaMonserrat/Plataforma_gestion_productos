from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from .models import Producto

def home(request):
    return render(request, "home.html")

@login_required
@permission_required("producto.view_producto", raise_exception=True)
def listado_productos(request):
    productos = Producto.objects.all()
    return render(request, "producto/listado.html", {"productos": productos})

@login_required
def solo_superuser(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    return render(request, "home.html")

def custom_403(request, exception=None):
    return render(request, "403.html", status=403)