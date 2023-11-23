from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Song, Favourite, History



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
                messages.success(request, "Login successfull")
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
                return render(request, 'login.html', context)
        return render(request, 'login.html',context)
    else:
        messages.info(request, "You are already logged in.")
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
    if request.method=='POST':
        user=request.user
        fav_song=Favourite(user=user, song=song)
        if Favourite.objects.filter(user=user, song=song).exists():
            delete_fav=Favourite.objects.filter(user=user, song=song)
            delete_fav.delete()
            messages.info(request, "Remove from favourites")
        else:
            fav_song.save()
            messages.success(request, "Song added to favourites")
            # return redirect('listne_song', song.song_id)
    
    ## Add to history ##
    user=request.user
    hist_song=History(user=user, song=song)
    if History.objects.filter(user=user, song=song).exists():
        delete_hist=History.objects.filter(user=user, song=song)
        delete_hist.delete()
        hist_song.save()
    else:
        hist_song.save()

        
    context={}
    context['song']=song
    return render (request, 'listne_song.html', context)


@login_required(login_url='login')
def favourite(request):
    context={}
    favourite_obj=Favourite.objects.filter(user=request.user).all()
    context['fav_objs']=favourite_obj
    return render(request, 'favourite.html', context)


@login_required(login_url='login')
def history(request):
    context={}
    history_obj=History.objects.filter(user=request.user).all()
    context['hist_objs']=history_obj
    return render(request, 'history.html', context)

def search_song(request):
    context={}
    query=request.GET['search-field']
    context['query']=query
    songs_obj=Song.objects.all()
    query_songs=songs_obj.filter(name__icontains=query)
    context['query_songs']=query_songs
    return render(request, 'search_result.html', context)