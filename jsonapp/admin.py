from typing import NamedTuple
from django.contrib import admin
from django.contrib.admin.decorators import display
from jsonapp import models 
class message(admin.ModelAdmin):
    list_display=['message','created_at','owner']
    NamedTuple={'owner':'from'}
# Register your models here.
admin.site.register(models.message,message)