"""
Example of how to download a TikTok video using the DownloadTikTokVideos class
"""

from download_tiktok_videos import DownloadTikTokVideos

URL = 'https://www.tiktok.com/@ray.amv000/video/7273108118777662725'

downloader = DownloadTikTokVideos()

downloader.download_video(URL)
