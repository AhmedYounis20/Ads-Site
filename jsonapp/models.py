from django.db import models
from django.conf import settings
from django.db.models.fields import DateTimeField
# Create your models here.
class message(models.Model):
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    message=models.TextField()
    created_at=DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message+' from '+self.owner.username
