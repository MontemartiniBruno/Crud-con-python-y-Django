from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hola(request):
    return HttpResponse('Hola mundo')

def home(request):
    return render(request, 'libreria/base.html')