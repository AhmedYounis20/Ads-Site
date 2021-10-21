from django.urls import path
from . import views

app_name ="ads"
urlpatterns=[
    path('ad/<int:pk>',views.DetailAdView.as_view(),name='ad_detail'),
    path('ad/<int:pk>/image',views.file_stream,name='ad_image'),
    path('ad/create',views.CreateAdView.as_view(),name='ad_create'),
    path('ad/<int:pk>/update',views.UpdateAdView.as_view(),name='ad_update'),
    path('ad/<int:pk>/delete',views.DeleteAdView.as_view(),name='ad_delete'),
    path('ads/',views.ListAdView.as_view(),name='ad_list'),
    path('ad/<int:pk>/favorite',views.favorite,name='favorite'),
    path('ad/<int:pk>/unfavorite',views.unfavorite,name='unfavorite'),
    path('',views.ListAdView.as_view(),),
    path('ad_picture/<int:pk>',views.file_stream,name='ad_image'),
    path('ad/<int:pk>/comment',views.CreateComment,name='ad_comment'),
    path('comment/<int:pk>/delete',views.DeleteComment.as_view(),name='delete_comment'),
    ]