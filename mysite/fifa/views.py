from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# from django_countries.fields import CountryField
from .soccerPlayer import SoccerPlayer
from .database import database
import random
import time





# db = database(reset=True)
db = database(reset=True)

def index(request):
    return HttpResponse("Hello, world. This is fifa app.")

def homepage(request):
    return render(request, 'homepage.html',{})

def add(request):
    return render(request, 'add.html',{})

def analytics(request):
    return render(request, 'analytics.html',{})

def map(request):
    lst = db.jsonData()
    myDict = {'result_list': lst}
    return render(request, 'map.html', myDict)

def ratings(request):
    lst = db.topAndLowestRated(100,True)
    myDict = {'result_list': lst}
    return render(request, 'ratings.html',myDict)

def ratings2 (request):
    lst = db.topAndLowestRated(100, False)
    myDict = {'result_list2': lst}
    return render(request, 'ratings2.html',myDict)

def comAge(request):
    lst = db.mostCommonAge()

    myDict = {'result_list': lst}
    return render(request, 'comAge.html',myDict)

def besthit(request):
    lst = db.bestHits(10,True)

    myDict2 = {'result_list': lst}


    return render(request, 'besthit.html',myDict2)

def mostPopularNation(request):
    labels=[]
    data=[]

    lst = db.PopularNation()
    myDict = {'result_list': lst}

    for player in myDict['result_list']:

         labels.append(player.nationname)
         data.append(player.numplayers)

    return render(request, 'mostPopularNation.html', {
            'labels': labels,
            'data': data,
        })



    # return render(request, 'mostPopularNation.html',myDict)


def mostPopularNation2(request):


    return render(request, 'mostPopularNation.html', )
def modify(request):
    print(request.GET)
    id = request.GET['modify_player']
    modify_player = db.searchEntry('player_id',id)[0]
    print('\n')
    print(modify_player)
    print(modify_player.name)
    print(type(modify_player))
    # for atr in modify_player:
    #     print(atr)
    print('\n')

    mydict = {'mod_id': modify_player.player_id,
              'mod_name': modify_player.name,
              'mod_nationality': modify_player.nationality,
              'mod_position': modify_player.position,
              'mod_overall': modify_player.overall,
              'mod_age': modify_player.age,
              'mod_hits': modify_player.hits,
              'mod_potential': modify_player.potential,
              'mod_team': modify_player.team}


    return render(request, 'modify.html',mydict)


def search(request):
     global playerName
     playerName=request.GET
     return render(request, 'search.html',playerName)


def modEntry(request):
     print('\n\n\n')
     for x in request.GET:
          print(f'{x}: {request.GET[x]}')
     print('\n\n\n')
     print(request.GET)
     rand_hits = random.randrange(1,20)

     db.modifyEntry(request.GET['player_id'],
                    request.GET['name'],
                    request.GET['nationality'],
                    request.GET['position'],
                    request.GET['rating'],
                    request.GET['age'],
                    str(rand_hits),
                    request.GET['potential'],
                    request.GET['club'],)

     return render(request, 'test.html',{'response':'modified'})


def delEntry(request):

     print('\n\n\n')
     for x in request.GET:
          print(f'{x}: {request.GET[x]}')
     print('\n\n\n')
     print(request.GET)

     id =  request.GET['player_id']
     db.deleteEntry(id)

     return render(request,'test.html',{'response':'deleted'})


def addResult(request):
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

     return render(request,'test.html', {'response':'added'})
     # return HttpResponse()

def team_ratings(request):
    t0 = time.time()
    team_list = db.teamAverageRating()
    t1 = time.time()
    duration = t1-t0

    print(f"\nteam ratings function duration: {duration}\n")
    return render(request,'teamRatings.html',{'team_list':team_list})


def test(request):
     for x in request.GET:
          print(f'{x}: {request.GET[x]}')

     searchstring=request.GET['SearchString']
     searchstring=searchstring.strip()

     attribute= request.GET['searchDrop']
     print(attribute)

#      if(attribute=='player_name'):
#           htmlPage = searchPlayerName(searchstring, df).to_html()

#
     lst=db.searchEntry(attribute,searchstring)

     myDict={'result_list':lst}

     return render(request, 'test.html',myDict)
     # return HttpResponse()

     # return render(request, 'test.html',{'dfPage':htmlPage})
