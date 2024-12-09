from django.urls import path
from .import views

app_name = 'wikiApp'

urlpatterns = [    
    path('',views.principal,name='principal'),    
    path('nuevoTema',views.nuevoTema,name='nuevoTema'),
    path('nuevoArticulo',views.nuevoArticulo,name='nuevoArticulo'),      
    path('articulos',views.articulos,name='articulos'),
    path('temas',views.temas,name='temas'),
    path('verTema/<str:idTema>',views.verTema,name='verTema') 
]