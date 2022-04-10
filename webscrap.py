#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
import re

resp = requests.get("https://eldenring.wiki.fextralife.com/Elden+Ring+Wiki")
content = resp.text

stripped = re.sub('<[^<]+?>', '', content)
print(stripped)
