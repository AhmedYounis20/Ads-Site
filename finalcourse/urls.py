"""finalcourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from ads import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),



    #### site apps 
    path('',include('ads.urls')),
    path('json/',include('jsonapp.urls')),
    path('favs/',include('favs.urls')),

    ### site logs
    ###### local sign
    path('accounts/login/',LoginView.as_view(template_name='ads/login.html')),
    path('accounts/logout/',LogoutView.as_view(),name='logout'),
    ########### oauth login 2 apps 
    path('accounts/', include('allauth.urls')),
    path('oauth/', include('social_django.urls',namespace='social')),
    




]
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
