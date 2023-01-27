from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObjectResolution = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObjectResolution.download()
    except:
        print('there has been an error in donwloading your youtube video')
    print('your video is downloaded')
link = input('put your youtube link here URL : ')
Download(link)