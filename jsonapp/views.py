from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.http import JsonResponse
import time
from django.views.generic.base import TemplateView
from jsonapp import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.contrib.humanize.templatetags import humanize 
from jsonapp.admin import message 
# Create your views here.
def main(request):
    return render(request,'json/main.html')

def jsonData(request):
    ## waiting time
    time.sleep(2)
    messages=models.message.objects.order_by('-created_at')[:10]
    message_list=[]
    for message in messages:
        message_list.append({'message':message.message,'from':message.owner.username,'created_at':humanize.naturaltime(message.created_at)} )
    data={
        "AUTHOR":{
        'first':'Ahmed',
        'last':'younis',
        'age':20,
        'hopies':['gym','programming','train birds']},
        "messages":message_list
        
    }
    return JsonResponse(data,safe=False)


class chat(LoginRequiredMixin,View):
    template_name='json/chat.html'
    def get(self,request):
        return render(request,'json/chat.html') 
    def post(self,request):
        if request.POST['message'].strip()!='':
            message=models.message(message=request.POST['message'].strip(),owner=request.user)
            message.save()
        return redirect('/json/chat')