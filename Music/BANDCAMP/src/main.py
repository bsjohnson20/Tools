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

    async def prepare_download(self, url):
        
        # url = ValueChangeEventArguments.value

        if not self.downloader.check_url_exists(url):
            self.container.clear()
            return
        self.downloader.url = url
        
        download_path = await run.cpu_bound(self.downloader.download, url)
        ui.notify("Download complete, zipping music...")
        path = await run.cpu_bound(self.downloader.zip_music, download_path)
        ui.notify("Zipping complete, downloading zip...")
        ui.download.file(path, "music.zip")
        ui.notify("Download complete")
        self.container.clear()

        



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
        box = ui.label()
        with box:
            box.url = url
            ui.table(rows=rows, row_key="title")
            ui.button("Delete", on_click=box.delete)
            ui.button("Download", on_click=lambda x: self.prepare_download(url))

    def setup_ui(self):
        # Title with Bandcamp Downloader
        ui.label("Bandcamp Downloader v0.0.1").classes("text-2xl font-bold")

        ui.label("Bandcamp URL (album/track/artist, example: https://bandcamp.com/album/album-name or https://bandcamp.com/track/track-name or https://bandcamp.com/artist/artist-name)").classes("text-lg")
        ui.label("Please enter the URL below").classes("text-lg")
        ui.input("Bandcamp URL", on_change=self.output_details).classes("w-1/2")


if __name__ in {"__main__", "__mp_main__"}:
    main()