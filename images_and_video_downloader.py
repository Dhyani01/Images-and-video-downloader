from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os
from pytube import YouTube


check=int(input("What thing you want to Download \n 1:IMAGES \n 2:YOUTUBE VIDEO\n"))

if check==1:
    def image():
        search=input("Enter images you want to search:-")
        folder_name=search.replace(" ","-").lower()
        parameter={"q":search}
        if not folder_name in os.listdir():
            os.makedirs(folder_name)
        r = requests.get("http://www.bing.com/images/search", params=parameter)
        soup=BeautifulSoup(r.text,"html.parser")
        links = soup.findAll("a", {"class": "thumb"})
        for item in links:
            try:
                img_obj = requests.get(item.attrs["href"])
                print("Getting", item.attrs["href"])
                Img_title = item.attrs["href"].split("/")[-1]
                try:
                    img = Image.open(BytesIO(img_obj.content))
                    img.save("./" + folder_name + "/" + Img_title, img.format)
                except:
                    print("Download for the wallpaper failed ! ")
            except:
                print("Download for the wallpaper failed !")
        image()
    image()

elif check==2:

        search=input("Enter the YouTube video name you want to download:-")
        folder_name=search.replace(" ","-").lower()
        parameter={"search_query":search}
        if not folder_name in os.listdir():
            os.makedirs(folder_name)
        dir_path = os.path.dirname(os.path.realpath(__file__))+ "\ ".strip()+folder_name
        r = requests.get("https://www.youtube.com/results", params=parameter)
        soup=BeautifulSoup(r.text,"html.parser")
        vids = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
        videolist=[]
        try:
            for v in vids:
                tmp = 'https://www.youtube.com' + v['href']
                YouTube(tmp).streams.first().download(dir_path)
        except:
            print("could not get the video")
else:
    print("Wrong Choice")
