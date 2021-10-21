from django.urls import path 

from jsonapp import views

app_name='json'
urlpatterns=[

    path('main/',views.main,name='main'),
    path('data',views.jsonData,name='main'),
    path('chat',views.chat.as_view(),name='chat'),

]