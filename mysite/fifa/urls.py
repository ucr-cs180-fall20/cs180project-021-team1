from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #url(r'^admin/', admin.site.urls),
    path('homepage/', views.homepage, name='homepage'),
    path('homepage/add/', views.add, name='add'),
    path('homepage/map/', views.map, name='map'),
    path('homepage/ratings/', views.ratings, name='ratings'),
    path('homepage/search/', views.search, name='search'),
    path('homepage/test/', views.test, name='test'),

    # path('navbar/',views.navbar, name='navbar'),
    #url(r'^homepage/', views.homepage),
]
