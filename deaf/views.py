from django.shortcuts import render, HttpResponse
from .models import video

# Create your views here.
def index(request):
    return render(request,'index.html')

def videos(request):
    #if request.method=="GET":
        # data1=video.objects.all()
        #return render(request, 'videos.html','''{'data1':data1}''')
    return render(request, 'videos.html')

def channel(request):
    return render(request,'channel.html')
    
def login(request):
    return render(request,'login.html')

def upload(request):
    return render(request,'upload.html')

def signup(request):
    return render(request,'signup.html')

def popup(request):
    return render(request,'popup.html')

def profile(request):
    return render(request,'popup.html')