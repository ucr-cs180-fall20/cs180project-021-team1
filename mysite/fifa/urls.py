from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #url(r'^admin/', admin.site.urls),
    path('homepage/', views.homepage, name='homepage'),
    path('homepage/add/', views.add, name='add'),
    path('homepage/search/', views.search, name='search'),
    path('homepage/map', views.map, name='map'),

    path('homepage/ratings/', views.ratings, name='ratings'),
    path('homepage/ratings2/', views.ratings2, name='ratings2'),
    path('homepage/comAge/', views.comAge, name='comAge'),
    path('homepage/besthit/', views.besthit, name='besthit'),
    path('homepage/teamRatings/', views.team_ratings, name='teamratings'),
    path('homepage/mostPopularNation/', views.mostPopularNation, name='mostPopularNation'),

    path('homepage/search/test/', views.test, name='test'),
    path('homepage/add/addResult', views.addResult, name='addResult'),
    path('homepage/search/test/delEntry', views.delEntry, name='delEntry'),
    path('homepage/search/test/modEntry', views.modEntry, name='modEntry'),
    path('homepage/search/test/modify', views.modify, name='modify')

    #url(r'^homepage/', views.homepage),
]
