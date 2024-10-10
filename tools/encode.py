
import os
presets = [[235, 320, 240, 30], [375, 384, 288, 30], [560, 512, 384, 30]]

path = './videos/'
for video_d in os.listdir('./v/'):
    video_dir = path + video_d + '/'
    os.makedirs(video_dir)
    index = 0
    print(video_dir)
    for video in os.listdir('./v/' + video_d + '/'):
        video_filename = './v/' + video_d + '/' + video
        m_video = str(index)
        os.makedirs(video_dir + m_video + '/Compressed/')
        index += 1
        for i, p in enumerate(presets):
            # '\BigBuckBunny\Compressed\320x240_fps30_420_235k.mp4'
            out_filename = video_dir + m_video + '/Compressed/' + \
                str(i) + '.mp4'
            os.system('ffmpeg -i \"' + video_filename +
                      '\" -y -r ' + str(p[3]) + ' -s ' + str(p[1]) + 'x' + str(p[2]) +
                      ' -an -c:v libx264 -x264opts keyint=' + str(2 * p[3]) + ':min-keyint=' + str(2 * p[3]) +
                      ':no-scenecut -b:v ' + str(p[0]) + 'k -maxrate ' + str(p[0]) +
                      'k -bufsize ' + str(p[0]) + 'k -r ' + str(p[3]) + ' ' + out_filename)
