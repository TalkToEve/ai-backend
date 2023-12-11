import os
import requests
from urllib.parse import urlparse
from collections import defaultdict
from bs4 import BeautifulSoup
import json

def clean_url(url: str):
    return url.replace("https://", "").replace("/", "-").replace(".", "_")

def get_response_and_save(url: str):
    response = requests.get(url)
    if not os.path.exists("./scrape"):
        os.mkdir("./scrape")
    parsed_url = clean_url(url)
    with open(f"./scrape/{parsed_url}.html", "wb") as f:
        f.write(response.content)
    return response

def scrape_links(scheme: str, origin: str, path: str, depth=10, sitemap=defaultdict(lambda: "")):
    site_url = f"{scheme}://{origin}{path}"
    cleaned_url = clean_url(site_url)

    if depth < 0:
        return
    if sitemap[cleaned_url] != "":
        return

    sitemap[cleaned_url] = site_url
    response = get_response_and_save(site_url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a")

    for link in links:
        href = urlparse(link.get("href"))
        if (href.netloc != origin and href.netloc != "") or (href.scheme != "" and href.scheme != "https"):
            continue
        scrape_links(href.scheme or "https", href.netloc or origin, href.path, depth=depth - 1, sitemap=sitemap)
    
    return sitemap

def scrape_site(site_url, depth=10):
    url = urlparse(site_url)
    sitemap = scrape_links(url.scheme, url.netloc, url.path, depth=depth)
    with open("./scrape/sitemap.json", "w") as f:
        f.write(json.dumps(sitemap))
