# Github Star fetcher using html parsing for awesome lists

I found it was annoying clicking links on awesome lists to find how many people used them so I could sort by that. So I built this, it's a python based script which uses github's api to fetch the number of stars for each repo in an awesome list, fetched by parsing the html from wget downloaded html files.

## Installation

```bash
uv sync
```

## Usage

```bash
wget <github_awesome_list_url> -o page.html
```

Open the Jupyter notebook and run the cells.

