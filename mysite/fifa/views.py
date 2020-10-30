from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .soccerPlayer import df
from .soccerPlayer import searchPlayerName,searchPlayerAge,searchPlayerRating,searchPlayerNationality,searchPlayerPosition,searchPlayerTeam
from .database import database as fDB
import random


playerName = None



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
     global playerName
     playerName=request.GET



     return render(request, 'search.html',playerName)

     #htmlPage = df.to_html()
     # return render(request, 'search.html')
     #return HttpResponse(htmlPage)

# def navbar(request):
#      return render(request, 'navbar.html')

def addResult(request):
     db = fDB()

     print('\n\n\n')
     for x in request.GET:
          print(f'{x}: {request.GET[x]}')
     print('\n\n\n')

     rand_id = str(random.randrange(300000,400000))
     name = request.GET['name']
     age = request.GET['age']
     nationality = request.GET['nationality']
     club = request.GET['club']
     rating = request.GET['rating']
     potential = request.GET['potential']
     position = request.GET['position']
     hits = "1"

     db.addEntry(rand_id,name,nationality,position,rating,age,hits,potential,club)

     return render(request,'test.html', {'player_name':name})


def listTest(request):
     print('\n\n\n')

     for x in request.GET:
          print(f'{x}: {request.GET[x]}')

     print('\n\n\n')

     searchstring = request.GET['SearchString']
     searchstring = searchstring.strip()

     attribute = request.GET['searchDrop']
     print(attribute)

     if (attribute == 'player_name'):
          myDf = searchPlayerName(searchstring, df)

     if (attribute == 'age'):
          htmlPage = searchPlayerAge(searchstring, df).to_html()

     if (attribute == 'nationality'):
          htmlPage = searchPlayerNationality(searchstring, df).to_html()

     if (attribute == 'club'):
          htmlPage = searchPlayerTeam(searchstring, df).to_html()

     if (attribute == 'rating'):
          htmlPage = searchPlayerRating(searchstring, df).to_html()

     if (attribute == 'position'):
          htmlPage = searchPlayerPosition(searchstring, df).to_html()

     print("\n\n")
     print(myDf)
     print("\n\n")
     for item in myDf.at():
          for subItem in item:
               print(subItem)


     myDf = ['one','two','three','four']

     return render(request, 'test.html',{'dfPage':myDf})



def test(request):

     print('\n\n\n')

     for x in request.GET:
          print(f'{x}: {request.GET[x]}')

     print('\n\n\n')


     searchstring=request.GET['SearchString']
     searchstring=searchstring.strip()

     attribute= request.GET['searchDrop']
     print(attribute)

     if(attribute=='player_name'):
          htmlPage = searchPlayerName(searchstring, df).to_html()

     if(attribute=='age'):
          htmlPage = searchPlayerAge(searchstring, df).to_html()

     if (attribute == 'nationality'):
          htmlPage = searchPlayerNationality(searchstring, df).to_html()

     if (attribute == 'club'):
          htmlPage = searchPlayerTeam(searchstring, df).to_html()

     if (attribute == 'rating'):
          htmlPage = searchPlayerRating(searchstring, df).to_html()

     if (attribute == 'position'):
          htmlPage = searchPlayerPosition(searchstring, df).to_html()

     print("\n\n")
     print(htmlPage)
     print("\n\n")


     return HttpResponse(htmlPage)
     # return render(request, 'test.html',{'dfPage':htmlPage})
