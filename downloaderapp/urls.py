from django.urls import path
from .views import ytdl, igdl, ttdl,youtube_dl, yt_download_done, get_insta , decide

app_name = 'downloaderapp'
urlpatterns = [
    path('', ytdl, name='youtubeapp'),
    path('download/', youtube_dl, name='quality'),
    path('download/<resolution>/',yt_download_done,name='yt_done'),
    path('instagram/',igdl, name='instagramapp'),
    path('get_insta/',get_insta,name='get_insta'),
    path('tiktok/', ttdl, name='tiktokapp'),
    path('decide/',decide, name='decide')
]