from django.urls import path
from . import views
urlpatterns = [
 path('contactUs', views.contactUs,name='contactUs'),
 path('contactus', views.contactUs,name='contactUs'),

]