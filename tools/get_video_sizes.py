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
        print(video_filename)
        if not os.path.exists(video_filename + 'size'):
            os.makedirs(video_filename + 'size')
            # assume baseline: 1920x1080_fps30_420_4300k
            baseline_dir = video_filename + 'DASH/1920x1080_fps30_420_4300k/'
            p_len = len(os.listdir(baseline_dir))
            for _p in range(p_len):
                # p 1.m4s
                p = str(_p + 1) + '.m4s'
                video_chunk = baseline_dir + p
                for df in DASH_FILE:
                    df_chunk = video_filename + 'DASH/' + df + '/' + p
                    f = open(video_filename + 'size/' + df, 'a')
                    chunk_size = os.path.getsize(df_chunk)
                    f.write(str(chunk_size) + '\n')
                    f.close()
