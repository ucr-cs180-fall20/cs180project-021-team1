from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. This is fifa app.")

def homepage(request):
#    return HttpResponse('homepage')
     return render(request, 'homepage.html')
