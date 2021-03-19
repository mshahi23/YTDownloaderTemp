from pytube import Playlist
from moviepy.editor import *
import os

bad_chars = ['/', "\\", ':', '*', '?', '"', '<', '>', '|', "'", "."]
# Output type
download_status = True
gif_status = False
mp3_status = False
delete_original = False


def intro(url, filetype):
    global link
    global delete_original
    global download_status
    global gif_status
    global mp3_status

    if not url == "":
        link = url
    else:
        return 1
    if filetype == "mp4":
        delete_original = False
    if filetype == "mp3":
        mp3_status = True
    if filetype == "gif":
        gif_status = True
    if filetype == "":
        return 2

    try:
        p = Playlist(link)
    except:
        return 3

    printString = "Downloaded:" + "\n"
    for video in p.videos:
        print(f'Downloading: {video.title}')
        # print(video.streams.all())
        trackName = video.title
        if download_status:
            path_mp4 = './mp4'
            missing_dir(path_mp4)

            for i in bad_chars:
                trackName = trackName.replace(i, '')
            printString = printString + trackName + "\n"
            mp4_file = './mp4/%s.mp4' % trackName
            video.streams.filter().first().download(path_mp4)
            our_video = VideoFileClip(mp4_file)
            our_audio = our_video.audio
            if mp3_status:
                path_mp3 = './mp3'
                missing_dir(path_mp3)
                mp3_file = './mp3/%s.mp3' % trackName
                our_audio.write_audiofile(mp3_file)
            if gif_status:
                path_gif = './gif'
                missing_dir(path_gif)
                gif_file = './gif/%s.gif' % trackName
                our_video.write_gif(gif_file)
            try:
                our_audio.close()
                our_video.close()
            except:
                pass
        if delete_original:
            os.remove('./mp4/%s.mp4' % trackName)

    return printString


def missing_dir(dir_path):
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
        message = "You are missing a directory so we made it for you"
        return message
