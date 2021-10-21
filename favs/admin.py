from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from favs import models
# Register your models here.

admin.site.register(models.thing)
admin.site.register(models.fav)
