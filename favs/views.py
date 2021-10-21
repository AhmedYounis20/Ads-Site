from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView,ListView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from favs import models 
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

class CreateThingView(CreateView,LoginRequiredMixin):
    model=models.thing
    template_name='favs/CreateThing.html'
    fields=['title','text']
    def form_valid(self, form):
        thing=form.save(commit = False)
        thing.owner=self.request.user
        thing.save()        
        return super().form_valid(form)

class UpdateThingView(UpdateView,LoginRequiredMixin):
    model=models.thing
    template_name='favs/CreateThing.html'
    fields=['title','text']
    def get_queryset(self) :
        return super().get_queryset().filter(owner=self.request.user)
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['update']=True
        return data
    

    
class DeleteThingView(DeleteView,LoginRequiredMixin):
    model=models.thing
    template_name='favs/DeleteThing.html'
    def get_queryset(self) :
        return super().get_queryset().filter(owner=self.request.user)
    success_url='/favs'
class DetailThingView(DetailView,LoginRequiredMixin):
    model=models.thing
    template_name='favs/DetailThing.html'
class ListThingView(ListView):
    def get(self,request):
        things=models.thing.objects.all()
        favorite_list=[]
        if request.user.is_authenticated :
            favorite_list=self.request.user.favorite_things.values('id')
            favorite_list=[fav['id'] for fav in favorite_list]
        data={"thing_list":things,'favorite_list':favorite_list}
        return render(request,'favs/ListThing.html',data)
@login_required
@method_decorator(csrf_exempt,name='dispatch')
def favorite(request,pk):
    thing=get_object_or_404(models.thing,pk=pk)
    fav=models.fav(user=request.user,thing=thing)
    fav.save()
    return HttpResponse()
@login_required
@method_decorator(csrf_exempt,name='dispatch')
def unfavorite(request,pk):
    thing=get_object_or_404(models.thing,pk=pk)
    fav=models.fav.objects.get(user=request.user.id,thing=thing)
    fav.delete()
    return HttpResponse()