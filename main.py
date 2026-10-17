from pytubefix import YouTube
from sys import argv

# variables
link = argv[1]
yt = YouTube(link)


#testing if code works
print("Title: ", yt.title)

print("View: ", yt.views)

youtube_download = yt.streams.get_highest_resolution()

# if video can't be downloaded, download audio instead mothafucka
if youtube_download is None:
    print("Video not available, downloading audio only💅🏾")
    youtube_download = yt.streams.get_audio_only()

youtube_download.download('/Users/Marcy_Student/Desktop/Youtube Videos')