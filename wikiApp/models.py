from django.db import models

# Create your models here.

class temaWiki(models.Model):
    nombreTema = models.CharField(max_length=128,null=True,blank=True)
    descripcionTema = models.CharField(max_length=512,null=True,blank=True)

class articuloWiki(models.Model):
    tituloArticulo = models.CharField(max_length=128,null=True,blank=True)
    contenidoArticulo = models.CharField(max_length=1024,null=True,blank=True)
    temaR = models.ForeignKey(temaWiki, null=True,blank=True, on_delete=models.SET_NULL) 