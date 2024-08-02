"""
This module provides functionality to download TikTok videos without watermarks.

Example:
    >>> from download_tiktok_videos import DownloadTikTokVideos
    >>> URL = 'https://www.tiktok.com/@ray.amv000/video/7273108118777662725'
    >>> downloader = DownloadTikTokVideos()
    >>> video_path = downloader.download_video(URL)

Methods:
    download_video(url: str) -> str: Downloads the TikTok video without watermarks.

Author: https://github.com/Pablo-Restrepo
"""

import os
from time import sleep
from bs4 import BeautifulSoup
import requests


class DownloadTikTokVideos:
    """
    This class provides functionality to download TikTok videos without watermarks.
    Attributes:
        BASE_URL (str): The base URL for downloading TikTok videos.
        HEADERS (dict): The headers to be used in the HTTP requests.
    Methods:
        __init__(): Initializes an instance of the DownloadTikTokVideos class.
        __get_download_link(url: str) -> str: Retrieves the download link for a TikTok video.
        __download_video(link: str) -> bytes: Downloads the video from the given link.
        download_video(url: str) -> str: Downloads the TikTok video without watermarks.
    """

    BASE_URL = 'https://ssstik.io/abc?url=dl'
    HEADERS = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0"
    }

    def __init__(self):
        pass

    def __get_download_link(self, url) -> str:
        """
        Retrieves the download link for a TikTok video.
        Args:
            url (str): The URL of the TikTok video.
        Returns:
            str: The download link for the TikTok video without watermarks,
                 or None if the link cannot be retrieved.
        """

        data = {'id': url, 'locale': 'es', 'tt': 'UERKR1dk'}
        try:
            response = requests.post(
                self.BASE_URL, data=data, headers=self.HEADERS, timeout=30)

            if response.status_code != 200:
                print(f'Request failed. Status code: {response.status_code}')

            soup = BeautifulSoup(response.content, 'html.parser')
            link_element = soup.find('a', string='Sin marca de agua')

            if link_element:
                return link_element.get('href')

            print('You tried to download another video very quickly.')
            return None
        except Exception as e:
            print(f'An error occurred: {str(e)}')
            return None

    def __download_video(self, link) -> bytes:
        """
        Downloads the video from the given link.
        Args:
            link (str): The download link for the TikTok video without watermarks.
        Returns:
            bytes: The video data as bytes, or None if the video cannot be downloaded.
        """

        try:
            response = requests.get(link, headers=self.HEADERS, timeout=70)

            if response.status_code == 200:
                return response.content

            print(f'Failed to download. Status code: {response.status_code}')
            return None

        except Exception as e:
            print(f'An error occurred: {str(e)}')
            return None

    def download_video(self, url: str) -> str:
        """
        Downloads a TikTok video from the given URL and saves it locally.
        Args:
            url (str): The URL of the TikTok video.
        Returns:
            str: The file path of the downloaded video.
        Raises:
            None
        """

        print(f'Downloading {url}...')
        download_link = self.__get_download_link(url)

        if download_link is None:
            print('Trying again in 10 seconds...')
            sleep(10)
            download_link = self.__get_download_link(url)

        if download_link is None:
            print('Unable to get the download link.')
            return None

        video_data = self.__download_video(download_link)

        if video_data is None:
            print('Unable to get the video.')
            return None

        current_dir = os.path.dirname(os.path.abspath(__file__))
        video_path = os.path.join(current_dir, 'video.mp4')

        try:
            count = 1
            while os.path.exists(video_path):
                video_path = os.path.join(current_dir, f'video ({count}).mp4')
                count += 1

            with open(video_path, 'wb') as file:
                file.write(video_data)
        except Exception as e:
            print(f'An error occurred: {str(e)}')
            return None

        print('Download successful.')
        return video_path
