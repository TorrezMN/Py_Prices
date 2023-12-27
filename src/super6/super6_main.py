# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

import json
import requests
from bs4 import BeautifulSoup
import datetime
import time
import ast
from random import randint, choice, uniform
from time import sleep

# Importing helpers.
from super6_engine import run_super6

import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
#super6_base_url = "https://www.superseis.com.py/default.aspx"
super6_base_url = "https://www.superseis.com.py/default.aspx"
super6_cats = {}


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}


def get_current_month_and_year():
    """Returns the current month and year in the format year-month."""
    now = datetime.datetime.now()
    month = now.month
    year = now.year
    return f"{year}-{month:02d}"


def get_current_date():
    """Returns the current date in the format dd/mm/yy."""
    today = datetime.date.today()
    return f"{today.day}/{today.month}/{today.year % 100}"


def get_current_time():
    """Returns the current time in the format HH:MM:SS."""
    now = datetime.datetime.now()
    return f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}"


def pprint_data(d):
    """Prints nicely a dict."""
    data = json.dumps(d, indent=4, ensure_ascii=False)
    print(data)


def get_data():
    """Gets page content."""
    response = requests.get(super6_base_url, headers=headers)
    return response.content


def super6_main():
    soup = BeautifulSoup(get_data(), "html.parser")
    menu = soup.find("div", attrs={"class": "wsmenu-submenu"})
    menu_items = menu.find_all('a')
    item_products = soup.find_all('div', attrs={'class':'item-box'})
    for i in menu_items:
        if i.has_attr('href'):
            super6_cats[i.text] = i['href']

    

if __name__ == "__main__":
    super6_main()
    for i in range(0, 10):
        random_delay = int(uniform(1, 15))
        print(f"RUNNING THE {i} ROUND.")
        print(f"Waiting {random_delay} seconds to continue.")
        time.sleep(random_delay)
        cat = choice(list(super6_cats.items()))
        run_super6(cat)
