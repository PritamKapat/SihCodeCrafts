from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='index-page'),
    path('job/',views.job, name='job-page'),
    path('learn/',views.learn, name='learn-page'),
    path('profile/',views.profile, name='profile-page'),
]