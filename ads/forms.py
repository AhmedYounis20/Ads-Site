from django import forms
from django.forms import fields

from ads import models

from django.core.files.uploadedfile import InMemoryUploadedFile

class CreateAdForm(forms.ModelForm):
    max_upload_limit=5*1024*1024
    max_limit_text='5M'
    image=forms.FileField(required=False,label='File to upload <= '+max_limit_text) 
    upload_field_name='image'
    class Meta:
        model=models.Ad
        fields=['title','price','text','tags','image']
    
    def clean(self):
        cleaned_data=super().clean()
        img=cleaned_data.get('image')
        if img is None:   return 
        if len(img)> self.max_upload_limit:
            self.add_error('image','file must be <='+ self.max_limit_text)
    

    def save(self,commit=True):
        instance=super(CreateAdForm,self).save(commit=False)
        file=instance.image
        if isinstance(file,InMemoryUploadedFile):
            bytearr=file.read();
            instance.content_type= file.content_type
            instance.image=bytearr
        if commit:
            instance.save()
            self.save_m2m()
        return instance