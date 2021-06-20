from pytube import YouTube 
# link of the video to be downloaded 
link=input("Provide Link")
yt = YouTube(link) 

# get the video with the extension and
# resolution passed in the get() function 
#d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
my_video = yt.streams.get_highest_resolution()
my_video.download()
