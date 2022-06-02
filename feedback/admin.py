from django.contrib import admin
from .models import Contact_us

# Register your models here.
class By_admin(admin.ModelAdmin):
 list_display=('id','name','email','created_date','message')
 

admin.site.register(Contact_us,By_admin)