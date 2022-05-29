from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('contactUs', views.contactUs,name='contactUs'),
    path('contactus', views.contactUs,name='contactus'),
    path('about', views.about,name='about'),
    path('store', views.store,name='store'),
    path('portfolio', views.portfolio,name='portfolio'),
]