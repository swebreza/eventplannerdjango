from django.urls import path
from . import views
urlpatterns = [
 path('portfolio', views.portfolio,name='portfolio'),
 path('blog', views.portfolio,name='blog'),

 path('blog_detail/<slug:slug>/', views.blog_detail,name='blog_detail'),
 # path('<slug:slug>/', views.blog_detail,name='blog_detail'),
]