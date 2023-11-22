from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Song



# Create your views here.
def index(request):
    context={}
    song= Song.objects.all()
    context['songs']=song
    return render(request, 'index.html', context)


def login_user(request):
    context={}
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
                return render(request, 'login.html', context)
        return render(request, 'login.html',context)
    else:
        messages.info(request, "you are already logged in.")
        return redirect('home')

def signup(request):
    context={}
    if not request.user.is_authenticated:
        if request.method == "POST":
            first_name=request.POST['firstname']
            lastname=request.POST['lastname']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1==password2:
                if User.objects.filter(username=username).exists():
                    messages.error(request, "Username already exists")
                elif User.objects.filter(email=email).exists():
                    messages.error(request, "Email already registered")
                else:
                    user = User(username=username, email=email)
                    user.first_name = first_name
                    user.last_name = lastname
                    user.set_password(password1)
                    user.save()

                    print("user created")
                    print(user)
                    user= authenticate(username=username, password=password1)
                    if user is not None:
                        login(request,user)
                        messages.success(request, "Account created successfully")
                        return redirect('home')
                    else:
                        messages.error(request, "Invalid login")               
            else:
                messages.error(request, "Passwords do not match")
        
        return render(request, 'signup.html',context)
    else:
        return redirect('home')

def logout_user(request):
    logout(request)
    messages.info(request, "Successfully logged out.")
    return redirect('home')

@login_required(login_url='login')
def songs(request):
    context={}
    song= Song.objects.all()
    context['songs']=song
    return render(request, 'songs.html',context)

@login_required(login_url='login')
def play_song(request, song_id):
    song=Song.objects.filter(song_id=song_id).first()
    context={}
    context['song']=song
    return render (request, 'listne_song.html', context)
