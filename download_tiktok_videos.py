import os
from time import sleep
import requests
from bs4 import BeautifulSoup


BASE_URL = "https://ssstik.io/abc?url=dl"
HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0"
}


class DownloadTikTokVideos:
    def __init__(self):
        pass

    def __get_download_link(self, url) -> str:
        data = {"id": url, "locale": "es", "tt": "UERKR1dk"}
        try:
            response = requests.post(
                BASE_URL, data=data, headers=HEADERS, timeout=30)

            if response.status_code != 200:
                print(f"Request failed. Status code: {response.status_code}")

            soup = BeautifulSoup(response.content, 'html.parser')
            link_element = soup.find('a', string='Sin marca de agua')

            if link_element:
                return link_element.get('href')

            print("You tried to download another video very quickly.")
            return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    def __download_video(self, link) -> bytes:
        try:
            response = requests.get(link, headers=HEADERS, timeout=70)

            if response.status_code == 200:
                return response.content

            print(f"Failed to download. Status code: {response.status_code}")
            return None

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    def download_video(self, url: str) -> str:
        print(f"Downloading {url}...")
        download_link = self.__get_download_link(url)

        if download_link is None:
            print("Trying again in 10 seconds...")
            sleep(10)
            download_link = self.__get_download_link(url)

        if download_link is None:
            print("Unable to get the download link.")
            return None

        video_data = self.__download_video(download_link)

        if video_data is None:
            print("Unable to get the video.")
            return None

        current_dir = os.path.dirname(os.path.abspath(__file__))
        video_path = os.path.join(current_dir, 'video.mp4')

        try:
            count = 1
            while os.path.exists(video_path):
                video_path = os.path.join(current_dir, f'video ({count}).mp4')
                count += 1

            with open(video_path, "wb") as file:
                file.write(video_data)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

        print("Download successful.")
        return video_path
