from pytube import YouTube

url = 'https://www.youtube.com/watch?v=zIr_d1ZsIGQ'

if __name__ == '__main__':
    yt = YouTube(url)

    # itag 139 -> audio/mp4
    stream = yt.streams.get_by_itag(139)
    stream.download()
