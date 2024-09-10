from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='index-page'),
    path('job/',views.job, name='job-page'),
    path('home2/',views.home2, name='home2-page'),
    path('learn/',views.learn, name='learn-page'),
    path('profile/',views.profile, name='profile-page'),
]