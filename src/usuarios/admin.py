from django.contrib import admin

# Register your models here.
from .models import Usuarios, Experiencia, Educacion, Habilidades, Logros

class UsuariosModelAdmin(admin.ModelAdmin):
    #Indicamos que columnas queremos ver : 
    list_display = ("__str__", "IdUsuario", "ImagUsua", "EstaUsua")
    #Agregamos una barra de busqueda:
    search_fields = ('IdUsuario', 'GeneUsua', 'CeluUsua', 'TeleUsua',)
    #Podemos agregar un filtro:
    list_filter = ('IdUsua', 'GeneUsua',)
    #Mostramos las fechas de creación del usuario:
    readonly_fields = ('RegiUsua',)
    #Indicamos desde donde se obtiene estos parametros:
    class Meta:
        model = Usuarios
admin.site.register(Usuarios, UsuariosModelAdmin)

class ExperienciaModelAdmin(admin.ModelAdmin):
    #Indicamos que columnas queremos ver:
    list_display = ("__str__", "CargExpe", "EmprExpe", "FechInic", "FechaFin", "SopoExpe")
    #Agregamos una barra de busqueda:
    search_fields = ('CargExpe', 'EmprExpe',)
    #Podemos agregar un filtro:
    list_filter = ('CargExpe','FechaFin',)
    #Mostramos las fechas de creación del usuario:
    readonly_fields = ('EstaExpt',)
    #Indicamos desde donde se obtienen estos parametros:
    class Meta:
        model = Experiencia
admin.site.register(Experiencia, ExperienciaModelAdmin)

class EducacionModelAdmin(admin.ModelAdmin):
    #Inidcamos que columnas queremos ver:
    list_display = ("__str__", "TipoEstu", "TituloEst", "FechGrado", "Instituto", "SoporteEs")
    #Agreamos una barra de busqueda:
    search_fields  = ('TituloEst', 'TipoEstu',)
    #Podemos agregar un filtro:
    list_filter = ('TipoEstu', 'FechGrado',)
    #Mostramos las fechas de creación del usuario:
    readonly_fields = ('EstaEstu',)
    #Indicamos desde donde se obtienen estos parametros:
    class Meta:
        model = Educacion
admin.site.register(Educacion, EducacionModelAdmin)

class LogrosModelAdmin(admin.ModelAdmin):
    #Indicamos que columnas queremos ver:
    list_display = ("__str__", "NombLogr", "FechLogr", "NombTilo")
    #Agregamos una barra de busqueda:
    search_fields = ('NombLogr','NombTilo','FechLogr',)
    #Podemos agregar un filtro:
    list_filter = ('NombTilo', 'FechLogr', 'NombLogr',)
    #Mostramos las fechas de creacion del usuario:
    #Readonly_fields = ('EstaEstu',)
    #Indicamos desde donde se obtienen estos parametros:
    class Meta:
        model = Logros
admin.site.register(Logros, LogrosModelAdmin)

class HabilidadesModelAdmin(admin.ModelAdmin):
    #Indicamos que colimnas queremos ver:
    list_display  =("__str__", "NombHabil", "NiveHabil")
    #Agregamos una barra de busqueda:
    search_fields = ('NombHabil','NiveHabil',)
    #Podemos agregar un filtro:
    list_filter = ('NiveHabil','NombHabil',)
    #Mostramos las fechas de creacion del usuario:
    #readonly_fields('EstaEstu',
    #Indicamos desde donde se obtienen estos parametros:
    class Meta:
        model = Habilidades
admin.site.register(Habilidades, HabilidadesModelAdmin)