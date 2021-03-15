# sudo apt install python3-pip -y
# pip install pytube
from pytube import *

url = "https://www.youtube.com/watch?v=a0TkeUhcVrM"
yt = YouTube(url)
video = yt.streams #to check video list
video_file=yt.streams.filter(progressive=True).first() #to fetch first audio and video file.
audio_file=yt.streams.filter(only_audio=True).first() #to fetch first audio file.
thumbnail=yt.thumbnail_url #to fetch thumbnail of video.
title=yt.title
desc=yt.description[:200] #to fetch description of vidio from 0 to 200 keywords.
print(video)
# video_file.download() #to download video file.