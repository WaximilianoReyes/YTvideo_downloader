import os
import certifi
import subprocess
from pytubefix import YouTube
import imageio_ffmpeg
from sys import argv


# variables
link = argv[1]
yt = YouTube(link)

# fixes that bullshit SSL error
os.environ["SSL_CERT_FILE"] = certifi.where()

#testing if code works
print("Title: ", yt.title)

print("View: ", yt.views)

youtube_download = yt.streams.get_highest_resolution()

# if video can't be downloaded, download audio instead mothafucka
if youtube_download is None:
    print("Video not available, downloading audio only💅🏾")
    youtube_download = yt.streams.get_audio_only()

youtube_download.download('/Users/Marcy_Student/Desktop/Youtube Videos')

# convert audio to .wav
file_path = os.path.join('/Users/Marcy_Student/Desktop/Youtube Videos', youtube_download.default_filename)


wav_path = os.path.splitext(file_path)[0] + ".wav"

# using ffpeg to do the converting
ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

subprocess.run([ffmpeg, "-y", "-i", file_path, "-vn", wav_path])

print("Done! Saved to:", wav_path)
print("Thank you for using indefinite downloads!")