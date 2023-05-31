import praw
import time
from RedDownloader import RedDownloader
import requests
import os

def slow_print(text, delay):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def intro():

    print("This is Ishitori\n")

    print("A simple terminal-based Anime Wallpaper Downloader\n")

    print("It uses reddit and praw to able to download static images, reddit and RedDownloader for live wallpapers\n\n")

def praw_images():

    command = str(input("Do you want live wallpapers(y/n):- "))

    search = str(input("Enter your search:- "))

    reddit = praw.Reddit(

           client_id="X.X.X.X",
           client_secret="X.X.X.X",
           user_agent="X.X.X.X"

)

    global sub

    if command == 'y':

        sub = "AnimewallpaperGif"

        i = 0

        print(search)

        subreddit = reddit.subreddit(sub)

        for submission in subreddit.search(search):

            url = "https://reddit.com"+submission.permalink

            # print(url)

            i = str(i)

            RedDownloader.Download(url , output=i , destination="../booru/vids/")        

            i = int(i)

            i += 1

    elif command == 'n':

        sub = "Animewallpaper"

        already_done = []

        i = 0

        subreddit = reddit.subreddit(sub)

        for submission in subreddit.search(search):

            # print(submission.url)

            result = submission.url

            if '.jpg' in submission.url:

                if submission.link_flair_text == "Desktop":

                    if submission.id not in already_done:

                        already_done.append(result)

                        # results.append(submission.url)

                        i = str(i)

                        with open('../booru/pics/'+i+'.jpg' , 'wb') as f:
                            response = requests.get(result)
                            f.write(response.content)
                        print("Image saved successfully")

                        i = int(i)

                        i += 1

                    else:
                        print("Image downaloaded skipping")

                else:
                    print("Skipped because wrong flair")

            else:
                print("Skipped wrong file type")

    else:

        print("Invalid command")

    

def is_image_file(file_path):

    extension = os.path.splitext(file_path)[1].lower()
    return extension == '.jpg' or extension == '.png'

intro();

praw_images();
