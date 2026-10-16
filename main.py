from pytubefix import YouTube
from sys import argv

# variables
link = argv[1]
yt = YouTube(link)


#testing if code works
print("Title: ", yt.title)

print("View: ", yt.views)