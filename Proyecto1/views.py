from django.http import HttpResponse

from django.template import Template, context

def saludo(request):
	return HttpResponse("Hola Django – Coder")

def segunda_vista(request):
	return HttpResponse("ya entendimos esto, es muy simple : ) ")

def miNombreEs(self, nombre):
	documentoDeTexto = f"Mi nombre es: <br><br> {nombre}"
	return HttpResponse(documentoDeTexto)

def probandoTemplate(self):
	miHtml = open(r"C:\Users\mauro\OneDrive\Escritorio\PythonProyecto1\Proyecto1\plantillas")
	plantilla = Template(miHtml.read())
	miHtml = context()
	miContexto = complex()
	documento = plantilla.render(miContexto)
	return HttpResponse(documento)
