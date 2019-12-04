from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from parametros.models import TipoDocu, Empleos, EStaCivil, Etnia, TipoLogr, TipoEstu


# Create your models here.

class Usuarios(models.Model):
    IdUsuario = models.CharField(max_lenght = 50, verbose_name = "No. Identificación", default="")
    idTipoDocu = models.ForeignKey(TipoDocu, default="", on_delete=models.CASCADE, verbose_name="Tipo de documento")
    idEstaCivil = models.ForeignKey(EStaCivil, default="", on_delete=models.CASCADE, verbose_name="Estado Civil")
    idEtnias  = models.ForeignKey(Etnia, default="", on_delete=models.CASCADE, verbose_name="Etnias")
    ImagUsua = models.ImageField(verbose_name = "Foto de Perfil", upload_to = "perfiles/img")
    PerfilPro = RichTextField(default="Candidato...", verbose_name = "Perfil Profesional")
    GeneUsua = models.CharField(max_lenght = 1, default="O", verbose_name = "Género")
    TeleUsua = models.CharField(max_lenght = 20, default="0", verbose_name = "Telefóno")
    CeleUsua = models.CharField(max_lenght = 20, default="0", verbose_name = "Celular")
    DireUsua = models.TextField(default="0", verbose_name = "Dirección Postal")
    RegiUsua = models.DateTimeField(default=0, auto_now_add = False, verbose_name  = "Registrado el:")
    EstaUsua  = models.CharField(max_lenght = 50, default="Activo", verbose_name = "Estado")

    class Meta:
        verbose_name  = "Candidato"
        verbose_name_plural = "Candidatos"

    #Ya creada la clase, retornamos el objeto NombEtni, o Nombre de Etnia:
    def __str__(self):
        return self.IdUsuario

    #Clase para la experiencia
    class Experiencia(models.Model):
        #Atributos de la clase experiencia:
        CargExpe = models.ForeignKey(Empleos, on_delete=models.CASCADE, limit_choices_to={'EsCargo': 'SI'}, verbose_name="Cargo Ocupado")
        EmprExpe = models.CharField(max_lenght = 150, verbose_name="Empresa")
        TeleEmpr = models.CharField(max_lenght = 30, verbose_name="Telefono de contácto de la Empresa")
        JefeExpe = models.CharField(max_lenght = 30, verbose_name="Persona de contácto de la Empresa")
        FechInic = models.DateTimeField(auto_now_add = False, default=0, verbose_name="Fecha de Inicio")
        FechFin = models.DateTimeField(auto_now_add = False, default=0, verbose_name="Fecha de Terminación")
        FuncionE = RichTextField(verbose_name="Funciones Desempeñadas")
        LogrExpe = RichTextField(verbose_name="Logros alcanzados")
        SopoExpe = models.FileField(upload_to="Soportes/laboral", default="", verbose_name="Certificado Laboral")
        EstaExpt = models.CharField(max_lenght= 30, default="Activo", verbose_name="Estado de Experiencia")

        class Meta:
            verbose_name = "Experiencia"
            verbose_name_plural = "Experiencia Laboral"

        def __str__(self):
            return self.CargExpe

    #Clase para almacenar la educación del candidato:
    class Educacion(models.Model):
        TipoEstu = models.ForeignKey(TipoEstu, on_delete=models.CASCADE, default="", verbose_name="Tipo de Educación")
        Instituto = models.CharField(max_lenght= 30, default="Activo", verbose_name="Institución o Academia")
        TituloEst = models.CharField(max_lenght= 250, verbose_name="Titulo Obtenido")
        FechGrado = models.DateTimeField(auto_now_add = False, default=0, verbose_name="Fecha de Graduación")
        SoporteEs = models.FileField(upload_to="soportes/educación", default="", verbose_name="Soporte Educación")
        EstaEstu = models.CharField(max_lenght= 30, default="Activo", verbose_name="Estado de Educación")
        
        class Meta:
            verbose_name = "Educación"
            verbose_name_plural = "Estudios Registrados"

        def __str__(self):
            return self.TituloEst

    #Clase para almacenar los logros obtenidos
    class Logros(models.Model):
        NombTilo = models.ForeignKey(TipoLogr, on_delete=models.CASCADE, verbose_name="Tipo de Logro")
        FechLogr = models.DateTimeField(auto_now_add = False, default=0, verbose_name="Fecha de Culminación")
        NombLogr = models.CharField(max_lenght=100, default="Activo", verbose_name="Logro o Distición")
        DescLogr = RichTextField(verbose_name="Descripción o caracteristicas del Logro")

        class Meta:
            verbose_name = "Logros"
            verbose_name_plural = "Logros Obtenidos"
        
        def __str__(self):
            return self.NombLogr

    #Clase para almacenar las habilidades del candidato:
    class Habilidades(models.Model):
        NombHabil = models.CharField(max_lenght= 100, default="Activo", verbose_name="Habilidad" )
        NiveHabil = models.CharField(max_lenght= 20, default"Activo", verbose_name="Nivel de Habilidad")

        class Meta:
            verbose_name = "Habilidades"
            verbose_name_plural = "Habilidades y Competencias"
        
        def __str__(self):
            return self.NombHabil

