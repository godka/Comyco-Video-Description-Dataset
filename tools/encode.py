# 235, 320, 240, 30
# 375, 384, 288, 30
# 560, 512, 384, 30
# 750, 512, 384, 30
# 1050, 640, 480, 30
# 1750, 720, 480, 30
# 2350, 1280, 720, 30
# 3000, 1280, 720, 30
# 4300, 1920, 1080, 30
# 5800, 1920, 1080, 30
# 7000, 1920, 1080, 30
import os
#import numpy as np
# cmd = ['ffmpeg -pix_fmt yuv420p -r ' num2str(representation{i, 4}) ' -s ' num2str(representation{i, 2}) 'x' ...
#    num2str(representation{i, 3}) ' -i ' path representation{i, 6} ...
#    ' -an -c:v libx264 -x264opts keyint=' num2str(2*representation{i, 4}) ':min-keyint=' num2str(2*representation{i, 4}) ...
#    ':no-scenecut -b:v ' num2str(representation{i,1}) 'k -maxrate ' num2str(representation{i,1}) ...
#    'k -bufsize ' num2str(representation{i,1}) 'k -r ' num2str(representation{i, 4}) ' ' path representation{i,7}];
presets = [[235, 320, 240, 30], [375, 384, 288, 30], [560, 512, 384, 30], [750, 512, 384, 30],
           [1050, 640, 480, 30], [1750, 720, 480, 30], [
               2350, 1280, 720, 30], [3000, 1280, 720, 30],
           [4300, 1920, 1080, 30]]
# ,[5800, 1920, 1080, 30],[7000, 1920, 1080, 30]]
#presets = np.array(presets)
path = './videos/'
#os.makedirs(path)
for video_d in os.listdir('./v/'):
    # [games,movies]
    video_dir = path + video_d + '/'
    os.makedirs(video_dir)
    index = 0
    print(video_dir)
    for video in os.listdir('./v/' + video_d + '/'):
        video_filename = './v/' + video_d + '/' + video
        m_video = str(index)
        os.makedirs(video_dir + m_video + '/Compressed/')
        index += 1
        for p in presets:
            # '\BigBuckBunny\Compressed\320x240_fps30_420_235k.mp4'
            out_filename = video_dir + m_video + '/Compressed/' + \
                str(p[1]) + 'x' + str(p[2]) + '_fps' + \
                str(p[3]) + '_420_' + str(p[0]) + 'k.mp4'
            os.system('ffmpeg.exe -i \"' + video_filename +
                      '\" -y -r ' + str(p[3]) + ' -s ' + str(p[1]) + 'x' + str(p[2]) +
                      ' -an -c:v libx264 -x264opts keyint=' + str(2 * p[3]) + ':min-keyint=' + str(2 * p[3]) +
                      ':no-scenecut -b:v ' + str(p[0]) + 'k -maxrate ' + str(p[0]) +
                      'k -bufsize ' + str(p[0]) + 'k -r ' + str(p[3]) + ' ' + out_filename)
