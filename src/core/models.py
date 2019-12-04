from django.db import models
from ckeditor.fields import RichTextField
#Importamos la lista de tipos de mensajes:
from .pqrsf import PQRSF_CHOICES

# Create your models here.
class Contact(models.Model):
    email = models.EmailField(max_length = 50, verbose_name ="Correo electrónico")
    tipom = models.CharField(max_length = 50, choices=PQRSF_CHOICES, default="Petición", verbose_name = "Categoria")
    nombre = models.CharField(max_length = 250, verbose_name = "Nombre")
    msj = RichTextField(default="Quisiera", verbose_name = "Mensaje")

    # Subclase para organizar los nombres de acuerdo al diccionario que usemos:
    class Meta:
        verbose_name  = "Mensajes PQRSF"
        verbose_name_plural  = "Mensajes PQRSF"

    def __str__(self):
        return self.nombre 
