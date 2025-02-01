from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

def Homeview(request):
    return render(request,'home.html')
