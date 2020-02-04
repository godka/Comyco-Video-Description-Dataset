# Comyco Video Dataset

To better improve the Comyco’s generalization ability, we propose a video quality DASH dataset involves movies, sports, TV-shows, games, news and MVs. Specifially, we first collect video clips with highest resolution from Youtube, then leverage FFmpeg to encode the video by H.264 codec and MP4Box to dashify videos according to the encoding ladder of video sequences. 
The bitrate ladder is represented as {235, 375, 560, 750, 1050, 1750, 2350, 3000, 4300}kbps.
Each chunk is encoded as 4 seconds. During the trans-coding process, for each video, we measure VMAF, VMAF-4K and VMAF-phone metric with the reference resolution of 1920 × 1080 respectively. In general, the dataset contains 86 complete videos, with 394,551 video chunks and 1,578,204 video quality assessments.

For more details please check './tools/'.