from django.http import HttpResponse
from django.shortcuts import render, redirect
from pytube import YouTube
from instalooter.looters import PostLooter
import os
from . import functions


def ytdl(request):
    return render(request, 'downloaderapp/youtube.html')

def youtube_dl(request):
    global url 
    url = request.GET.get('url')
    yt = YouTube(url)
    video = []
    video = yt.streams.filter(progressive=True).all()
    embed = url.replace("watch?v=", "embed/")
    return render(request, 'downloaderapp/ytdl.html',{'video': video, 'embed':embed})

def yt_download_done(request, resolution):
    global url
    homedir = os.path.expanduser('~')
    dirs = homedir + '/Downloads'
    print(dirs)
    if request.method == 'POST':
        YouTube(url).streams.get_by_resolution(resolution).download(dirs)
        return render(request, 'downloaderapp/done.html')
    else:
        return render(request, 'downloaderapp/error.html')


def igdl(request):
    return render(request, 'downloaderapp/instagram.html')
 


def get_insta(request):
    link = request.POST.get('url')
    homedir = os.path.expanduser('~')
    dirs = homedir + '/Downloads'
    if request.method == 'POST':
        PostLooter(link).download(dirs)
        return render(request, 'downloaderapp/done.html')
    else:
        return render(request, 'downloaderapp/error.html')


def ttdl(request):
    return render(request, 'downloaderapp/tiktok.html')

def download(request,url):
    link = functions.downloader(url)
    return render(request, 'downloaderapp/tiktok.html', {"without_watermark": link})

def json(request,url):
    link = functions.downloader(url)
    return HttpResponse(link)

def decide(request):
    url = request.POST.get("url")
    return download(request,url)
  