# Simple py program that scans mods.yml to get installed files
# Sorts by last updated date so you can determine which mods might be the cause of bugs
# Uses cachier to store a physical cache and prevent duplicate requests




import requests
import yaml
import os
import datetime
from cachier import cachier
from bs4 import BeautifulSoup
import time
cachier = cachier(stale_after=datetime.timedelta(days=1), cache_dir='/tmp/.cache')

# load file
file = "~/.config/r2modmanPlus-local/LethalCompany/profiles/Default/mods.yml"
# expand path
file = os.path.expanduser(file)

@cachier
def load_mods():
    with open(file, 'r') as f:
        data = yaml.safe_load(f)
    mods = {}
    for item in data:
        mods[item['name']] = [item['name'], item['websiteUrl'], item['enabled']]
    mods = {k: v for k, v in mods.items() if v[2]}
    return mods

@cachier
def request_page(url):
    print("Requesting page...")
    response = requests.get(url)
    time.sleep(1)
    return response

def remove_tags(text):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text()

mods = load_mods()
count = {"total": len(mods), "current": 0}
parsed_mods = {}
for mod in mods:
    if mod == "Owen3H-CSync":
        continue
    # print(mods[mod])
    page = request_page(mods[mod][1])
    lines = page.text.split('\n')
    lines = [line.strip() for line in lines if line.strip()]
    for i, line in enumerate(lines):
        if "Last updated" in line:
            data = (remove_tags(line), remove_tags(lines[i+1]))
            parsed_mods[mod] = (data[1], mods[mod][1])
            # print(data)
            break
    count["current"] += 1
    print(count["current"], "/", count["total"])

def convert_to_days(date_str):
    # Convert "2 years ago" or "1 week ago"
    try:
        if "years" in date_str:
            return int(date_str.split(' ')[0]) * 365
        # a year ago
        elif "year" in date_str:
            return 1 * 365
        elif "weeks" in date_str:
            return int(date_str.split(' ')[0]) * 7
        elif "week" in date_str:
            return 1 * 7
        elif "months" in date_str:
            return int(date_str.split(' ')[0]) * 30
        elif "month" in date_str:
            return 1 * 30
        elif "days" in date_str:
            return int(date_str.split(' ')[0])
        elif "day" in date_str:
            return 1
        else:
            return 0
    except ValueError:
        print("Invalid date format", date_str)

mods = [[mod, convert_to_days(parsed_mods[mod][0]), parsed_mods[mod][1]] for mod in parsed_mods]
mods.sort(key=lambda x: x[1])
for mod in mods:
    print(mod[0], mod[1], mod[2])
