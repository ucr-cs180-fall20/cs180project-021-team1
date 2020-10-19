from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. This is fifa app.")

#def homepage(request):

 #    return render(request, 'homepage.html')

def homepage(request):

     print(request.POST)
     return render(request, 'homepage.html')

def homepage(request):
     print(request.GET)
     print('Your request has been recieved ')
     return render(request, 'homepage.html')



