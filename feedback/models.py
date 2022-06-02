from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Contact_us(models.Model):
 name = models.CharField(max_length=255)
 email = models.EmailField()
 message = RichTextField(default='')
 created_date=models.DateTimeField(default=datetime.now,blank=True)
 class Meta:
  ordering = ('-id',)