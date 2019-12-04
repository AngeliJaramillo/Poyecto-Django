from django.shortcuts import render, HttpResponse, redirect
#Importamos el archivo urls para redireccionar:
from django.urls import reverse
#Cargamos el formulario:
from .forms import ContactForm

# Create your views here. Creamos nuestras vista index:

def indexcore(request):
    #Instanciamos el formulario de contacto:
    FormContact = ContactForm()
    #Validamos que se haya echo la petición post del formulario de contacto:
    if request.method == "POST":
        # Re asignamos el valor de FormContact, esta vez con todos los datos del formulario
        FormContact = ContactForm(data=request.POST)
        #Validaremos que todoslos campos sean del tipo de dato correcto:
        if FormContact.is_valid():
            #Retornamos los valoresde los campos:
            email = request.POST.get('email','')
            tipom = request.POST.get('tipom','')
            nombre = request.POST.get('nombre','')
            msj = request.POST.get('msj','')
            #Si todo sale bien, guardamos y redireccionamos al nombre de la url con un mensaje
            FormContact.save()
            return redirect(reverse('inicio')+"?OK")
    return render(request, 'core/index.html', { 'fornulario': FormContact})


def nosotros(request):
        return render(request, 'core/nosotros.html')
        