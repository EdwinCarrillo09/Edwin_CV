from django.contrib import admin
from django.urls import path
from cv.views import ver_cv, descargar_cv, ver_certificado 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ver_cv, name='hoja_de_vida'),
    path('descargar/', descargar_cv, name='descargar_cv'),
    path('certificado/<int:cert_id>/', ver_certificado, name='ver_certificado'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)