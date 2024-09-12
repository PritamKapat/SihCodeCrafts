from django.shortcuts import render
from groq import Groq

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

def message(msg):
    client = Groq(api_key="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")

    prompt = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a career adviser only."
            },
            {
                "role": "user",
                "content": msg
            }
        ],
    )
    
    ms = prompt.choices[0].message.content
    return ms
