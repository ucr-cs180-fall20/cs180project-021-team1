from django.shortcuts import render
from django.http import HttpResponse
from .soccerPlayer import df
from .soccerPlayer import searchPlayerName,searchPlayerAge,searchPlayerRating,searchPlayerNationality,searchPlayerPosition,searchPlayerTeam

playerName = None

def index(request):
    return HttpResponse("Hello, world. This is fifa app.")

def homepage(request):
    return render(request, 'homepage.html',{})

def add(request):
    return render(request, 'add.html',{})

def analytics(request):
    return render(request, 'analytics.html',{})
def map(request):
    return render(request, 'map.html',{})

def ratings(request):
    return render(request, 'ratings.html',{})


def search(request):
     global playerName
     playerName=request.GET
     return render(request, 'search.html',playerName)

# # def homepage(request):
# #      playerName=request.POST # playerName is the variable saved once searched. Use this to search Database.
# #      print(request.POST)
# #      print(playerName)
# #      return render(request, 'homepage.html')
# #
# def homepage(request):
#      playerName = request.GET #playerName is the variable saved once searched. Use this to search Database.
#      print(request.GET)
#      print(playerName)
#      print('Your request has been recieved ')
#      return render(request, 'homepage.html')

# def search(request):
#      global playerName
#      playerName=request.GET
#      return render(request, 'search.html',playerName)

#      #htmlPage = df.to_html()
#      # return render(request, 'search.html')
#      #return HttpResponse(htmlPage)


# def test(request):

#      print('\n\n\n')

#      for x in request.GET:
#           print(f'{x}: {request.GET[x]}')

#      print('\n\n\n')


#      searchstring=request.GET['SearchString']
#      searchstring=searchstring.strip()

#      attribute= request.GET['searchDrop']
#      print(attribute)

#      if(attribute=='player_name'):
#           htmlPage = searchPlayerName(searchstring, df).to_html()

#      if(attribute=='age'):
#           htmlPage = searchPlayerAge(searchstring, df).to_html()

#      if (attribute == 'nationality'):
#           htmlPage = searchPlayerNationality(searchstring, df).to_html()

#      if (attribute == 'club'):
#           htmlPage = searchPlayerTeam(searchstring, df).to_html()

#      if (attribute == 'rating'):
#           htmlPage = searchPlayerRating(searchstring, df).to_html()

#      if (attribute == 'position'):
#           htmlPage = searchPlayerPosition(searchstring, df).to_html()



#      return HttpResponse(htmlPage)
#      # return render(request, 'test.html')
