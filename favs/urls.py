from django.urls import path 
from favs import views


app_name='favs'
urlpatterns=[
    path('fav/<int:pk>',views.DetailThingView.as_view(),name='thing_detail'),
    path('fav/create',views.CreateThingView.as_view(),name='thing_create'),
    path('fav/<int:pk>/update',views.UpdateThingView.as_view(),name='thing_update'),
    path('fav/<int:pk>/delete',views.DeleteThingView.as_view(),name='thing_delete'),
    path('',views.ListThingView.as_view(),name='thing_list'),
    path('fav/<int:pk>/favorite',views.favorite,name='favorite'),
    path('fav/<int:pk>/unfavorite',views.unfavorite,name='unfavorite'),
]