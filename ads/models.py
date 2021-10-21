from django.db import models
from django.shortcuts import redirect
from django.urls.base import reverse
from django.utils.translation import TranslatorCommentWarning
from django.conf import settings
from taggit.managers import TaggableManager
# Create your models here.
class Ad(models.Model):
    title=models.CharField(max_length=150,)
    price=models.FloatField()
    text=models.TextField()
    favorites = models.ManyToManyField(settings.AUTH_USER_MODEL,
        through='adFav', related_name='favorite_ads',blank=True)
    tags=TaggableManager()
    ###### pics
    image=models.BinaryField(null=True,blank=True,editable=True)
    content_type=models.CharField(max_length=500,null=True,blank=True,help_text='the MIMEType of the file')

    ########
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    Updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def get_absolute_url (self):
        return reverse('ads:ad_detail',kwargs={'pk':self.pk})
class adFav(models.Model) :
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # https://docs.djangoproject.com/en/3.0/ref/models/options/#unique-together
    class Meta:
        unique_together = ('ad', 'user')

    def __str__(self) :
        return '%s likes %s'%(self.user.username, self.ad.title[:10])
class comment(models.Model):
    Author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    Updated_at=models.DateTimeField(auto_now=True)
    post=models.ForeignKey(to='Ad',on_delete=models.CASCADE,related_name='comments',null=True,blank=True)
    def __str__(self):
        return self.text
    def get_absolute_url(self):
        print(self.post.pk)
        return reverse('ads:ad_detail',kwargs={'pk':self.post.pk})
