from django.conf import settings

import requests as req
from bs4 import BeautifulSoup
import json


def downloader(link):
    source = "https://freevideosdowloader.tk/services/downloader_api.php"
    resp = req.post(source, data={"url": link}, verify=True).text
    links_list = json.loads(resp)["VideoResult"][0]["VideoUrl"]


  
    return links_list
