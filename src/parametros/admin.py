from django.contrib import admin

#Importamos cada una de las clases creadas en el archivo models.py:

from .models import Etnia
from .models import TipoDocu
from .models import EstaCivil
from .models import TipoEstu
from .models import TipoLogr

# Register your models here.

admin.site.register(Etnia)
admin.site.register(TipoDocu)
admin.site.register(EstaCivil)
admin.site.register(TipoEstu)
admin.site.register(TipoLogr)
