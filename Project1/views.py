from django.http import HttpResponse
from django.template import Context, Template

def teste(request):
    html = open(r'C:\Users\artco\OneDrive\Área de Trabalho\Python Coder\ProjetoDjango\Project1\Templates\teste.html')
    template = Template(html.read())
    html.close()
    context = Context()

    document = template.render(context)
    return HttpResponse(document)