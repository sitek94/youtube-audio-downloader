from pytube import Playlist

p = Playlist('https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n')

NUMBER_OF_FILES_TO_DOWNLOAD = 3

for video in p.videos[:NUMBER_OF_FILES_TO_DOWNLOAD]:
    stream = video.streams.get_by_itag(139)
    stream.download(output_path='downloads')
