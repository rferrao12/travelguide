from django.http import HttpResponse
from django.shortcuts import render
from . models import Destination

# Create your views here.

def index(request):
 destss = Destination.objects.all()
 return render(request,'index.html', {'destss': destss})