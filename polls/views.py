from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   return HttpResponse("hola desde la app de polls")

def hello(request):
    return HttpResponse("<h1>hello</h1>")