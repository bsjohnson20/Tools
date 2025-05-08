import functools
import os
import requests
import re
import logging as l
import urllib
import time
from functools import cache, wraps

def logger():
    logger = l.getLogger('bandcamp_dl')
    logger.setLevel(l.DEBUG)
    ch = l.StreamHandler()
    ch.setLevel(l.DEBUG)
    formatter = l.Formatter('[%(asctime)s - %(name)s - %(levelname)s]: %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
log = logger()

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        log.info(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

@timeit
@functools.lru_cache
def request(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request).read().decode('utf-8')
    return response

class BandcampPage:
    def __init__(self, url):
        self.url = url

    @functools.lru_cache
    def check_type(self, url=None) -> str:
        # Check whether it's track, album or artist
        """
        Checks whether the given url is a track, album or artist.
        
        Args:
            url (str): The url to check.
        
        Returns:
            str: The type of page, or "Error" if it can't be determined.
        """
        if url is None:
            url = self.url

        if "track" in url:
            return "track"
        elif "album" in url:
            return "album"
        elif re.match(r"https://(.*?).bandcamp.com", url) is not None:
            return "artist"
        return "Error"

    @functools.lru_cache
    def get_page(self):
        cache_path = f"{self.url}.html".replace("https://", "").replace("/", "-")
        cache_path = "/tmp/" + cache_path
        if os.path.exists(cache_path):
            with open(cache_path, "r") as f:
                log.info(f"Using cache file: {cache_path}")
                self.page = f.read()
                return True

        page = request(self.url)
        self.page = page
        
        # create offline cache of html
        with open(cache_path, "w") as f:
            f.write(page)
            log.info(f"Created cache file: {cache_path}")
        return True


    @functools.lru_cache
    def get_title(self):
        self.get_page()
        title = re.search('<title>(.*?)</title>', self.page).group(1)
        return title

    @functools.lru_cache
    def get_author(self):
        self.get_page()
        
        # Check if author in url <author>.bandcamp.com
        try:
            author = re.search('https://(.*?).bandcamp.com', self.url).group(1)
        except AttributeError:
            # Search html for author
            author = re.search('<meta name="author" content="(.*?)" />', self.page).group(1)

        return author
    
    def format_as_table(self):
        columns = [{
            "title": "Title",
            "artist_title": "Artist",
            "type": "Type",
        }]

        rows = [{
            "title": self.get_title(),
            "artist_title": self.get_author(),
            "type": self.check_type()
        }]

        return columns, rows


    @functools.lru_cache
    def debug(self):
        # Test what kind url is, what name, title, author etc
        self.get_page()
        functions = [self.get_title, self.check_type, self.get_author]
        for func in functions:
            log.info(func())

    

if __name__ == "__main__":
    page = BandcampPage("https://4everfreebrony.bandcamp.com/album/hoping-remastered")
    page.debug()