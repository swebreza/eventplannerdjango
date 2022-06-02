from gc import get_objects
from django.shortcuts import render,get_object_or_404
from .models import blogs
# Create your views here.


def blog_detail(request,slug):
 blog=get_object_or_404(blogs,pk=slug)
 data = {
  'post' : blog
 }
 return render(request,'webpages/blog_detail.html',data)



def portfolio(request):
 blog=blogs.objects.all
 data = {
  'post' : blog
 }
 return render(request,'webpages/portfolio.html',data)