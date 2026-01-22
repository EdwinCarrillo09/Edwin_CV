from django.shortcuts import render, get_object_or_404
from .models import Perfil, Experiencia, Habilidad, Referencia, Certificado

def ver_cv(request):    
    perfil = Perfil.objects.first()
    experiencias = Experiencia.objects.filter(perfil=perfil)
    habilidades = Habilidad.objects.filter(perfil=perfil)
    referencias = Referencia.objects.filter(perfil=perfil)
    certificados = Certificado.objects.filter(perfil=perfil)
    
    contexto = {
        'perfil': perfil,
        'experiencias': experiencias,
        'habilidades': habilidades,
        'referencias': referencias, 
        'certificados': certificados, 
    }
    return render(request, 'cv/index.html', contexto)


def ver_certificado(request, cert_id):
    # Esta función busca el certificado y lo muestra
    certificado = get_object_or_404(Certificado, id=cert_id)
    return render(request, 'cv/certificado.html', {'certificado': certificado})

def descargar_cv(request):
    # Por ahora, para que no te de error, esta función abrirá la vista de impresión
    # del navegador, que es la forma más fácil de guardar como PDF.
    perfil = Perfil.objects.first()
    return render(request, 'cv/index.html', {'perfil': perfil, 'modo_impresion': True})