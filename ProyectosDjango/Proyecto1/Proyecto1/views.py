from datetime import datetime
from multiprocessing import context
from re import template
from xml.dom.minidom import Document
from django.http import HttpResponse

def saludo(request):
	return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
	return HttpResponse("<br><br>Ya entendimos esto, es muy simple")


def diaDeHoy(request):
    dia = datetime.now()
    documentoDeTexto = f"Hoy es día:<br>{dia}"
    return HttpResponse(documentoDeTexto)

def miNombreEs(self,nombre):
	documentoDeTexto = f"Mi nombre es <br><br> {nombre}"
	return HttpResponse(documentoDeTexto)

def probandoTemplate(self):
   miHtml = open("C:\Users\Rocio\OneDrive\Documents\De nico\Nico CODER\ProyectosDjango\Proyecto1\Plantillas\templatel.html")
   plantilla = template(miHtml.read()) #Se carga en memoria nuestro documento,templatel
   ## 030 importar templateycontex,con:from django.template import Template,Context
   miHtml.close() #Cerramos el archivo
   miContexto = context() #EN este caso no hay nada ya que no hay parametros,IGUAL hay que crearlo
   documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento
   return HttpResponse(documento)