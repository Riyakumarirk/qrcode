import ssl
from pytube import YouTube
ssl._create_default_https_context = ssl._create_unverified_context

link = "https://www.youtube.com/watch?v=6ZwwapPikyQ&ab_channel=MLRecords"
youtube_1 = YouTube(link)

#print(youtube_1.title)
#print(youtube_1.thumbnail_url)
videos= youtube_1.streams.all()
vi=list(enumerate(videos))
for i in vi:
    print(i)
strm=int(input("Enter :  "))
videos[strm].download()
print("succesful")

