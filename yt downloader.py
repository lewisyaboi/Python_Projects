import pytube
from pytube import YouTube


video = YouTube('https://youtu.be/1_sNa6q__lA')

video_streams = video.streams
print(video_streams)
