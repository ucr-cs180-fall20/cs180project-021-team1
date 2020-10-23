from django.shortcuts import render
from django.http import HttpResponse
from .soccerPlayer import df


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

def add(request):
     return render(request, 'add.html')


def map(request):
     return render(request, 'map.html')


def ratings(request):
     return render(request, 'ratings.html')

#NOTE: comment line 41, uncoment line 43 and 45 to see entire dataset
def search(request):

     # player_name=request.POST
     # print(player_name)
     return render(request, 'search.html')

     #htmlPage = df.to_html()
     # return render(request, 'search.html')
     #return HttpResponse(htmlPage)

# def navbar(request):
#      return render(request, 'navbar.html')