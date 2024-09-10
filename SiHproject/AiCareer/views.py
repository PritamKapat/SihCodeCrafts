from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")
def job(request):
    return render(request, "jobtrend.html")
def learn(request):
    return render(request, "learn.html")
def profile(request):
    return render(request, "profile.html")
def home2(request):
    return render(request, "home2.html")