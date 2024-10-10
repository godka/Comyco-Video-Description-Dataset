import os
from natsort import natsorted

for video in os.listdir('./videos/'):
    for seg in natsorted(os.listdir('./videos/' + video + '/')):
        video_filename = './videos/' + video + '/' + seg + '/'
        os.makedirs(video_filename + 'DASH/')
        cmd = 'MP4Box -dash 4000 -segment-name %s\\ -rap -out ' + video_filename + 'DASH/' + seg + '.mpd'
        for p in  os.listdir(video_filename + 'Compressed/'):
            cmd += ' ' + video_filename + 'Compressed/' + p
        os.system(cmd)
