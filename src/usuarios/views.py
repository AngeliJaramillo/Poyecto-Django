from django.shortcuts import render, get_object_or_404
#Agregamos las librerias necesarias para trabajar con vistas basadas en clases (CVB):
from django.views.generic.base import TemplateView
#Agregamos la libreria para importar listviews
from django.views.generic.list import ListView
#Importamos nuestros modelos:
from .models import Usuarios, Experiencia, Logros, Habilidades, Educacion


