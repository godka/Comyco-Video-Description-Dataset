# vmafossexec.exe yuv420p 1920 1080 out.yuv out2.yuv model/vmaf_v0.6.1.pkl --log out.xml --thread 8 -subsample 5
# ffmpeg -i 320x240_fps30_420_235k.mp4 -s 1920x1080 -pix_fmt yuv420p out.yuv
import os

DASH_FILE = ['320x240_fps30_420_235k', '384x288_fps30_420_375k',
             '512x384_fps30_420_560k', '512x384_fps30_420_750k',
             '640x480_fps30_420_1050k', '720x480_fps30_420_1750k',
             '1280x720_fps30_420_2350k', '1280x720_fps30_420_3000k',
             '1920x1080_fps30_420_4300k']

for t in os.listdir('./videos/'):
    # videos/games
    video_dir = './videos/' + t + '/'
    for v in os.listdir(video_dir):
        video_filename = video_dir + v + '/'
        if not os.path.exists(video_filename + 'vmaf'):
            os.makedirs(video_filename + 'vmaf')
        # assume baseline: 1920x1080_fps30_420_4300k
        baseline_dir = video_filename + 'DASH/1920x1080_fps30_420_4300k/'
        p_len = len(os.listdir(baseline_dir))
        for _p in range(p_len):
            # p 1.m4s
            p = str(_p + 1) + '.m4s'
            video_chunk = baseline_dir + p
            print('cat ' + video_filename + 'DASH/' + v + '_init.mp4 ' +
                      video_chunk + ' >> 3.mp4')
            os.system('cat ' + video_filename + 'DASH/' + v + '_init.mp4 ' +
                      video_chunk + ' >> 3.mp4')
            os.system('pause')