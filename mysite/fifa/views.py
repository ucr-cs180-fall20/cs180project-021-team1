from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. This is fifa app.")

# def homepage(request):
#     return render(request, 'homepage.html')

# def homepage(request):
#      playerName=request.POST # playerName is the variable saved once searched. Use this to search Database.
#      print(request.POST)
#      print(playerName)
#      return render(request, 'homepage.html')
#
def homepage(request):
     playerName = request.GET #playerName is the variable saved once searched. Use this to search Database.
     print(request.GET)
     print(playerName)
     print('Your request has been recieved ')
     return render(request, 'homepage.html')



