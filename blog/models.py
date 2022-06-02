from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify


# Create your models here.
class blogs(models.Model):
 category_choice=(
  ('birthday',"birthday"),
  ('anniversary',"anniversary"),
  ('proposal',"proposal"),
  ('party',"party"),
 )
 imgs = models.ImageField(upload_to='media/%Y/%m/')
 title = models.CharField(max_length=255)
 categorys = models.CharField(max_length=255,choices=category_choice)
 body = RichTextField(default='')
 created_date=models.DateTimeField(default=datetime.now,blank=True)
 slug = models.SlugField(null=False,unique=True)

 class Meta:
  ordering = ('-id',)
 #slug with unique values.
 # def save(self, *args, **kwargs):
 #  if not self.slug:
 #   self.slug = slugify(self.title)
 #  super().save(*args, **kwargs)