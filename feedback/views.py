from django.shortcuts import render
from .models import Contact_us
from django.contrib import messages

# Create your views here.
def contactUs(request):
 if request.method =='POST':
  name1=request.POST['name']
  email=request.POST['email']
  message=request.POST['message']
  formData=Contact_us(name=name1,email=email,message=message)
  formData.save()
  messages.success(request,"Submitted Successfully!! ")
 return render(request,'webpages/contactUs.html')