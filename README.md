# Download-TikTok-Videos-Without-Watermark

This project uses an external API to download TikTok videos without watermarks.

## Requirements

- Python
- pip

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/Pablo-Restrepo/Download-TikTok-Videos-Without-Watermark
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

# Usage
Here is an example of how to use the DownloadTikTokVideos class to download a TikTok video:

```python
from download_tiktok_videos import DownloadTikTokVideos

URL = 'https://www.tiktok.com/@ray.amv000/video/7273108118777662725'

downloader = DownloadTikTokVideos()
video_path = downloader.download_video(URL)
print(f'Video downloaded to: {video_path}')
```

You can also refer to the `example_download_videos.py` file for a complete example.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).