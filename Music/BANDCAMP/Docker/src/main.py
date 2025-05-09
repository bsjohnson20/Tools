from functools import partial
from multiprocessing import Value
from nicegui import ui, run
import metadata_fetcher
import download



class main:
    def __init__(self) -> None:
        self.container = ui.column()

        ui.run(port=8000)
        self.downloader = download.Downloader()

        self.setup_ui()


    def finish_download(self, path):
        ui.download.file(path, "music.zip")
        self.container.clear()

    async def prepare_download(self, url):
        with self.box:
            ui.spinner(size='lg')
        # url = ValueChangeEventArguments.value

        if not self.downloader.check_url_exists(url):
            self.container.clear()
            return
        self.downloader.url = url
        
        download_path = await run.cpu_bound(self.downloader.download, url)
        ui.notify("Download complete, zipping music...")
        path = await run.cpu_bound(self.downloader.zip_music, download_path)
        with self.box:
            ui.button("Download Complete. Grab music link:", on_click=partial(self.finish_download, path))
            
        



    def output_details(self, ValueChangeEventArguments):
        url = ValueChangeEventArguments.value
        if not self.downloader.check_url_exists(url):
            self.container.clear()
            return
        self.downloader.url = url
        self.container.clear()
        meta = metadata_fetcher.BandcampPage(url)
        columns, rows = meta.format_as_table()
        print(columns, rows)
        
        
        # Table with details
        self.box = ui.label()
        with self.box:
            self.box.url = url
            ui.table(rows=rows, row_key="title")
            ui.button("Delete", on_click=self.box.delete)
            ui.button("Download", on_click=lambda x: self.prepare_download(url))
            

            

    def setup_ui(self):
        # Title with Bandcamp Downloader
        ui.label("Bandcamp Downloader v0.0.2").classes("text-2xl font-bold")

        ui.label("Bandcamp URL (album/track/artist, example: https://bandcamp.com/album/album-name or https://bandcamp.com/track/track-name or https://bandcamp.com/artist/artist-name)").classes("text-lg")
        ui.label("Please enter the URL below").classes("text-lg")
        ui.input("Bandcamp URL", on_change=self.output_details).classes("w-1/2")


if __name__ in {"__main__", "__mp_main__"}:
    main()