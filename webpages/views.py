# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
 return render(request,'webpages/index.html')


def about(request):
 return render(request,'webpages/about.html')



def store(request):
 return render(request,'webpages/store.html')

