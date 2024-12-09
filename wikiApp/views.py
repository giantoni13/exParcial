from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import temaWiki,articuloWiki

# Create your views here.
def principal(request):
    return render(request,'principal.html',{
        'temaSistema':temaWiki.objects.all()
    })

def nuevoTema(request):
    if request.method =='POST':
        nombreTema = request.POST.get('nombreTema')
        descripcionTema = request.POST.get('descripcionTema')
        temaWiki.objects.create(
            nombreTema = nombreTema,
            descripcionTema = descripcionTema
        )
        return HttpResponseRedirect(reverse('wikiApp:temas'))
    return render(request,'nuevoTema.html',{
        'temaSistema':temaWiki.objects.all()
    })

def nuevoArticulo(request):
    if request.method =='POST':
        tituloArticulo = request.POST.get('tituloArticulo')
        contenidoArticulo = request.POST.get('contenidoArticulo')
        temaSeleccionado = request.POST.get('temaSeleccionado')
        temaObj = temaWiki.objects.get(id=temaSeleccionado)
        articuloWiki.objects.create(
            tituloArticulo = tituloArticulo,
            contenidoArticulo = contenidoArticulo,
            temaR=temaObj
        )
        return HttpResponseRedirect(reverse('wikiApp:articulos'))
    return render(request,'nuevoArticulo.html',{
        'temaSistema':temaWiki.objects.all()
    })

def temas(request):
    temasTotales = temaWiki.objects.all()
    return render(request,'temas.html',{
        'temasTotales':temasTotales,
        'articulosSistema':articuloWiki.objects.all(),
        'temaSistema':temaWiki.objects.all()
    })

def articulos(request):
    articulossTotales = articuloWiki.objects.all()
    return render(request,'articulos.html',{
        'articulosTotales':articulossTotales,
        'articulosSistema':articuloWiki.objects.all(),
        'temaSistema':temaWiki.objects.all()
    })

def verTema(request,idTema):
    temaInfo = temaWiki.objects.get(id=idTema)
    listaArticulos = temaInfo.articuloWiki_set.all()
    return render(request,'verTema.html',{
        'objTema':temaInfo,
        'temasSistema':temaWiki.objects.all(),      
        'listaArticulos':listaArticulos
    })