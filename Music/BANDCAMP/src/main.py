from nicegui import ui
from nicegui.events import ValueChangeEventArguments

from bs4 import BeautifulSoup
import requests
import re
from bandcamp_api import Bandcamp
bc = Bandcamp()
import subprocess as sp
import os
import shutil
# def show(event: ValueChangeEventArguments):
#     name = type(event.sender).__name__
#     ui.notify(f'{name}: {event.value}')

class main:

    def __init__(self):

        self.path = os.path.dirname(os.path.abspath(__file__))
        print(self.path)
        self.container = ui.column()

        # Title with Bandcamp Downloader
        ui.label("Bandcamp Downloader v0.0.1").classes("text-2xl font-bold")

        ui.label("Bandcamp URL (album/track/artist, example: https://bandcamp.com/album/album-name or https://bandcamp.com/track/track-name or https://bandcamp.com/artist/artist-name)").classes("text-lg")
        ui.label("Please enter the URL below").classes("text-lg")

        ui.input("Bandcamp URL", on_change=self.get_website_name).classes("w-1/2")


        ui.run(port=8000)

    def sanitise_url(self, url):
        # remove any non alphanumeric characters except &, - and .
        return re.sub(r'[^a-zA-Z0-9&-.]', '', url)

    def download(self, url):
        # bandcamp-downloader
        
        if os.path.exists("music"):
            shutil.rmtree("music")
        os.mkdir("music")
        print("Downloading music to: ", f"{self.path}/music/")
        command = ['uv', 'run', 'bandcamp-dl', "--base-dir="+self.path+"/music", url, "-re"]
        print("Running bandcamp with args: ", command)
        sp.run(command)
        # Check if music folder empty
        if not os.listdir(f"{self.path}/music"):
            ui.notify("Error: could not download music")
            self.container.clear()
            return
        sp.run(['7z', 'a', 'music.zip', 'music/*'])
        
        ui.notify("Download Complete")
        self.container.add_slot(ui.label("Download Complete. Grab music link:"))
        self.container.add_slot(ui.button("Fetch", on_click=lambda: ui.download.file("music.zip")))
        # add download link 

    def check_valid_url(self, url):
        url
        if "bandcamp.com" in url:
            return True
        else:
            return False

    

    def parse_website(self, url):

        if not self.check_valid_url(url):
            return

        # Check whether it's track, album or artist
        result = ""
        if "track" in url:
            result = bc.get_track(url)
        elif "album" in url:
            result = bc.get_album(url)
        elif "artist" in url:
            result = bc.get_artist(url)

        columns = {
            "track_title": "Track Title",
            "artist_title": "Artist",
            "album_title": "Album"
        }

        rows = {
            "track_title": result.track_title,
            "artist_title": result.artist_title,
            "album_title": result.album_title
        }

        with ui.row():
            t_container = ui.column()
            with t_container:
                x = ui.label(f"{columns['track_title']}: {rows['track_title']}").classes("text-lg")
                y = ui.label(f"{columns['artist_title']}: {rows['artist_title']}").classes("text-lg")
                z = ui.label(f"{columns['album_title']}: {rows['album_title']}").classes("text-lg")
                ui.button("Delete", on_click=lambda: t_container.delete()).classes("w-1/2")
                ui.button("Download", on_click=lambda: self.download(url)).classes("w-1/2")
            

    def get_website_name(self, ValueChangeEventArguments):
        url = ValueChangeEventArguments.value
        if not self.check_valid_url(url):
            return
        
        self.parse_website(url)

    

if __name__ in {"__main__", "__mp_main__"}:
    main()