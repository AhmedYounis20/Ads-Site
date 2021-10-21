from typing_extensions import Concatenate
from django.contrib import admin
from .models import *
# Register your models here.
class ads(admin.ModelAdmin):

    list_display=['title','price','created_at','image']
    ordering=['-Updated_at']
    exclude=['image','content_type']
admin.site.register(Ad,ads)
admin.site.register(comment)