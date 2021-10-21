from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse 
# Create your models here.
class thing(models.Model):
    title=models.CharField(max_length=500,validators=[MinLengthValidator(2,'please enter some greater title minimun length is 2 characters 😉')])
    text = models.TextField()
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    favorites=models.ManyToManyField(settings.AUTH_USER_MODEL,through='fav',related_name='favorite_things')
    created_at=models.DateTimeField(auto_now_add=True,)
    Updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('favs:thing_detail', kwargs={'pk':self.id})
class fav(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    thing=models.ForeignKey('thing',on_delete=models.CASCADE)


    class Meta:
        unique_together=['thing','user']

    def __str__(self) :
        return self.user.username+' likes ❤ '+self.thing.title[:10]
