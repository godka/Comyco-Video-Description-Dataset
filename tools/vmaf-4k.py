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
        if not os.path.exists(video_filename + 'vmaf-4k'):
            os.makedirs(video_filename + 'vmaf-4k')
        # assume baseline: 1920x1080_fps30_420_4300k
        baseline_dir = video_filename + 'DASH/1920x1080_fps30_420_4300k/'
        p_len = len(os.listdir(baseline_dir))
        for _p in range(p_len):
            # p 1.m4s
            p = str(_p + 1) + '.m4s'
            video_chunk = baseline_dir + p
            os.system('cat ' + video_filename + 'DASH/' + v + '_init.mp4 ' +
                      video_chunk + ' >> baseline.mp4')
            os.system(
                'ffmpeg -y -i baseline.mp4 -s 1920x1080 -pix_fmt yuv420p baseline.yuv')
            for df in DASH_FILE:
                df_chunk = video_filename + 'DASH/' + df + '/' + p
                os.system('cat ' + video_filename + 'DASH/' + v + '_init.mp4 ' +
                          df_chunk + ' >> out.mp4')
                os.system(
                    'ffmpeg -y -i out.mp4 -s 1920x1080 -pix_fmt yuv420p out.yuv')
                os.system(
                    'vmafossexec yuv420p 1920 1080 baseline.yuv out.yuv model/vmaf_4k_v0.6.1.pkl --log out.json --thread 0 >> out.log')
                # find vmaf
                f = open('out.log', 'r')
                for l in f:
                    sp = l.split(' = ')
                    if len(sp) == 2:
                        score = float(sp[-1])
                f.close()
                f = open(video_filename + 'vmaf-4k/' + df, 'a')
                f.write(str(score))
                f.write('\n')
                f.close()
                os.system('rm -rf out.mp4')
                os.system('rm -rf out.yuv')
                os.system('rm -rf out.log')
            os.system('rm -rf baseline.mp4')
            os.system('rm -rf baseline.yuv')
