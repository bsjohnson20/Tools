import functools
import re
import subprocess as sp
import logging as l
import time



def logger():
    logger = l.getLogger('bandcamp_dl')
    logger.setLevel(l.DEBUG)
    ch = l.StreamHandler()
    ch.setLevel(l.DEBUG)
    formatter = l.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
log = logger()



class Downloader:
    def __init__(self):
        self.url = None
        self.tmp_dir = None

    @functools.lru_cache
    def create_tmp(self, url)-> str:
        # create random tmp directory
        result = sp.Popen(['mktemp', '-d'], stdout=sp.PIPE, stderr=sp.PIPE)
        stdout, stderr = result.communicate()
        tmp_dir = stdout.decode('utf-8').strip()
        log.info("tmp dir: " + tmp_dir)
        return tmp_dir

    def check_url_exists(self, url):
        # Using requests with timeout took 20 seconds?? on nonexisting website urls
        # match https://xxx.bandcamp.com or https://bandcamp.com
        if re.match(r"https://(.*?).bandcamp.com", url) is None:
            return False
        return True
    
    def zip_music(self, tmp_dir) -> str:
        current_time = str(int(time.time()))
        file_name = current_time # generated based on time
        print("Zipping music: " + tmp_dir)
        process_7z = sp.Popen(['7z', 'a', f'/tmp/{file_name}.zip', f'{tmp_dir}/*']) #
        process_7z.wait()
        # return location of zip file
        return f'/tmp/{file_name}.zip'

    def download(self, url) -> bool:
        if not self.check_url_exists(url):
            return False
        self.tmp_dir = self.create_tmp(url)
        
        log.info("Downloading music to: " + self.tmp_dir)
        command = ['uv', 'run', 'bandcamp-dl', "--base-dir="+'.'+"/", url]
        log.info("Running bandcamp with args: " + str(command))
        process = sp.Popen(command, cwd=self.tmp_dir, stdout=sp.PIPE, stderr=sp.PIPE)
        output, error = process.communicate()
        if process.returncode != 0:
            log.info("Error: could not download music")
            return False
        return self.tmp_dir
    
# print(check_url_exists("https://bandcamap.com"))
# download("ASDASDSA")