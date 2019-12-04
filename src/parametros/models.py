from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
#Los modelos son una clase que devuelve un objeto,
#por lo que crearemos una clase con el nombre de la entidad o coleccion y definiremos los atributos:

#clase para el modelo Etnia, esta clase se encargará:
class Etnia(models.Model):
    NombreEtni=models.CharField(max_length = 50)
    # Clase para los meta archivos de la clase:
    class Meta:
        verbose_name = "Grupo Etnico"
        verbose_name_plural = "Grupos Etnicos"
        def __str__(self):
            return self.NombreEtni


    #Clase para el modelo TipoDocu
class TipoDocu(models.Model):
    NombreTiDo=models.CharField(max_length = 50)
    
    class Meta:
        verbose_name = "Tipo De Documento"
        verbose_name_plural = "Tipo De Documentos"
        
        def __str__(self):
            return self.NombreTiDo

    #clase estado civil

class EstaCivil(models.Model):
    NombEsCi=models.CharField(max_length = 50)
    
    class Meta:
        verbose_name = "Estado Civil"
        verbose_name_plural = "Estados Civiles"
        
        def __str__(self):
            return self.NombEsCi


   #Clase para la clasificación de estudios
class TipoEstu(models.Model):
    NombreTiEs=models.CharField(max_length = 50)

    class Meta:
        verbose_name = "Tipo De Estudio"
        verbose_name_plural = "Tipo De Estudios"
        
        def __str__(self):
            return self.NombreTiEs

    #Clase para tipos de logros   
class TipoLogr(models.Model):
    NombreTiLo=models.CharField(max_length = 50)
    
    class Meta:
        verbose_name = "Tipo De Logro"
        verbose_name_plural = "Tipo De Logros"
        
        def __str__(self):
            return self.NombreTiLo
