__author__ = "SakuraBlossomTree"

from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import os

def intro():

    print("This is Ishitori\n")

    print("A simple terminal-based Anime Wallpaper Downloader\n")

    print("It uses reddit and praw to able to download static images, reddit and RedDownloader for live wallpapers\n\n")

def images():
    tags = str(input("Enter your tags: "))

    limit = int(input("Enter your amount of pics: "))
    
    base_url = "https://safebooru.org/index.php?page=post&s=list&tags=" + tags

    print(base_url)

    response = requests.get(base_url)

    soup = BeautifulSoup(response.content , "html.parser")

    image_elements = soup.find_all("img" , class_="preview")

    count = 0

    for element in image_elements:

        if count >= limit:

            break

        image_page_url = urljoin(base_url , element.parent["href"])

        image_response = requests.get(image_page_url)

        image_soup = BeautifulSoup(image_response.content, 'html.parser')

        actual_image_element = image_soup.find('img' , id='image')

        if actual_image_element:

            actual_image_url = actual_image_element['src']
            print(actual_image_url)
            save_image(actual_image_url)
            count += 1

def save_image(url):

    response = requests.get(url)

    if response.status_code == 200:

        filename = url.split('/')[-1]

        with open(os.path.join('./pics/', filename) , 'wb') as f:
            f.write(response.content)
            print(f"Saved image: {filename}")

    else:

        print(f"Failed to download image: {url}")

intro();

images();

