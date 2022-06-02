from django.contrib import admin
from .models import blogs

# Register your models here.
class By_admin(admin.ModelAdmin):
 list_display=('id','title','created_date')
 

admin.site.register(blogs,By_admin)