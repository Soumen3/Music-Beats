from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('songs/', views.songs, name='songs'),
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name="logout"),
    path('songs/<int:song_id>/', views.play_song, name='listne_song'),
    path('songs/favourite/', views.favourite, name='fav'),
    path('songs/history/', views.history, name='history'),
    path('songs/search/',views.search_song, name='search')
]
