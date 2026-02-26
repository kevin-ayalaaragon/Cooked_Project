from django.urls import path
from . import views

urlpatterns = [
    # Empty string '' means this is the homepage (127.0.0.1:8000/)
    path('', views.recipe_search, name='recipe_search'),
    
    # We keep 'search/' as well so the old links don't break
    path('search/', views.recipe_search, name='recipe_search'),
    
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('my-kitchen/', views.my_kitchen, name='my_kitchen'),
    path('signup/', views.signup, name='signup'),
    path('community/', views.global_feed, name='global_feed'),
    path('recipe/<int:pk>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('kitchen/<str:username>/', views.user_kitchen, name='user_kitchen'),
    path('follow/<str:username>/', views.toggle_follow, name='toggle_follow'),
]