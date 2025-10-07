from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler403

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("producto.urls")),
]

handler403 = "producto.views.custom_403"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)