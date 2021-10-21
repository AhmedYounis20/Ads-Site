from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from ads import models,forms 
from django.views.generic import CreateView,UpdateView,DeleteView,ListView,DetailView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
class CreateAdView(View,LoginRequiredMixin):
    model=models.Ad
    template_name='ads/CreateAd.html'
    def get(self,request,pk=None):

        form=forms.CreateAdForm()
        context={'form':form}
        return render(request,self.template_name,context)

    def post(self,request,pk=None):
        form=forms.CreateAdForm(request.POST,request.FILES or None)
        if not form.is_valid():
            context={'form':form}
            return render(request,self.template_name,context)
        ad=form.save(commit=False)
        ad.author=request.user
        ad.save()
        return redirect(self.success_url)
    success_url='/ads'

# Create your views here.
class UpdateAdView(View,LoginRequiredMixin):
    model=models.Ad
    template_name='ads/CreateAd.html'
    success_url='/ads'

    def get(self,request,pk):
        ad=get_object_or_404(models.Ad,id=pk,author=self.request.user)
        form=forms.CreateAdForm(instance=ad)
        context={'form':form,'update':True}
        return render(request,self.template_name,context)

    def post(self,request,pk=None):
        ad=get_object_or_404(models.Ad,id=pk)
        form=forms.CreateAdForm(request.POST,request.FILES or None,instance=ad)
        if not form.is_valid():
            context={'form':form,'update':True}
            return render(request,self.template_name,context)
        ad=form.save(commit=False)
        ad.save()
        return redirect(self.success_url)
class DeleteAdView(DeleteView,LoginRequiredMixin):
    model=models.Ad
    template_name='ads/DeleteAd.html'
    success_url='/ads'
class DetailAdView(DetailView):
    model=models.Ad
    template_name='ads/DetailAd.html'
class ListAdView(ListView):
    def get(self,request):
        ads=models.Ad.objects.all()
        favorite_list=[]
        if request.user.is_authenticated :
            favorite_list=self.request.user.favorite_ads.values('id')
            favorite_list=[fav['id'] for fav in favorite_list]
        data={"ad_list":ads,'favorite_list':favorite_list}
        return render(request,'ads/ListAd.html',data)
def file_stream(request,pk):
    ad=get_object_or_404(models.Ad,id=pk)
    print(ad.content_type)
    response=HttpResponse()
    response['content-type']=ad.content_type
    response['content-length']=len(ad.image)
    response.write(ad.image)
    return response

@login_required
def CreateComment(request,pk):
    model=get_object_or_404(models.Ad,id=pk)
    if  request.method == 'POST':
        comment=models.comment(text=request.POST['comment'])
        comment.Author=request.user
        comment.post=model
        comment.save()
    return redirect('/ad/{}'.format(pk))
class DeleteComment(LoginRequiredMixin,DeleteView):
    model=models.comment
    template_name='ads/DeleteComment.html'
    def get_success_url(self):
        return reverse('ads:ad_detail',kwargs={'pk':self.get_context_data()['comment'].post.id})
    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        self.success_url=reverse('ads:ad_detail',kwargs={'pk':data['comment'].post.id})
        print(self.success_url)
        return data
@login_required
@method_decorator(csrf_exempt,name='dispatch')
def favorite(request,pk):
    ad=get_object_or_404(models.Ad,pk=pk)
    fav=models.adFav(user=request.user,ad=ad)
    fav.save()
    return HttpResponse()
@login_required
@method_decorator(csrf_exempt,name='dispatch')
def unfavorite(request,pk):
    ad=get_object_or_404(models.Ad,pk=pk)
    fav=models.adFav.objects.get(user=request.user.id,ad=ad)
    fav.delete()
    return HttpResponse()