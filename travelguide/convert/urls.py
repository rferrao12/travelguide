from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('conv', views.conv, name='conv'),
    path('add', views.add,name='add'),
    path('mal',views.mal, name='mal'),
    path('ind',views.ind, name='ind'),
    path('sri', views.sri, name='sri'),
    path('sing', views.sing, name='sing'),
    path('fran', views.fran, name='fran'),
    path('dub', views.dub, name='dub'),
    path('lon', views.lon, name='lon'),
    path('aus', views.aus, name='aus'),
    path('gre', views.gre, name='gre'),
    path('itl', views.itl, name='itl'),
    path('jap', views.jap, name='jap'),

]