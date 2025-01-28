#/bin/python3
from bs4 import BeautifulSoup as bs
import requests as r
# Path: main.py
def get_soup(html):
    return bs(html, 'html.parser')

def load_html(url):
    print(url)
    return r.get(url).text

def parse_git_stars(soup):
    return soup.find_all('a', id="repo-stars-counter-star", href=True)

# load html from file
with open("page.html","r") as f:
    html = f.read()

# parse the hrefs from the soup
soup = get_soup(html).find_all('a', href=True)

# store the hrefs in a list
hrefs = [a['href'] for a in soup if "#" not in a['href'] and "https://" in (a['href'])]
print(hrefs)
# check one of the hrefs' git stars
result = load_html(hrefs[0])
print(parse_git_stars(get_soup(result)))
