from . import views
from django.urls import path , include
from django.contrib import admin
urlpatterns = [
    path('home/',views.home, name='Home'),
    path('help/',views.help_,name='Help'),
    path('news/',views.dashboard,name='news'),
    path('news/<int:pk>/',views.homeDetail,name='homeDetail'),
    path('newpost/',views.newPostPage,name='NewPage'),
    path(route='',view=views.dashboard,name='dashboard'),
    path(route='', view=include('django.contrib.auth.urls')),
    path(route='register/', view=views.register, name='register'),
]