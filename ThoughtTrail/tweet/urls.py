from django.urls import path
from . import views

urlpatterns = [
    path('tweet/', views.tweet_list, name='tweet_list'),
    path('tweet/create/', views.tweet_create, name='tweet_create'),
    path('tweet/<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('tweet/<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),  
]
