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
from stock_engine import run_stock

import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
stock_base_url = "https://www.stock.com.py/default.aspx"
stock_cats = {}


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
    response = requests.get(stock_base_url, headers=headers)
    return response.content


def stock_main():
    soup = BeautifulSoup(get_data(), "html.parser")
    menu = soup.find_all("div", attrs={"class": "wsmenu-submenu"})
    # Sets the 'categories' to start the script.
    for i in menu[0].find_all("a"):
        if i.has_attr("href"):
            stock_cats[i.text] = i["href"]


if __name__ == "__main__":
    stock_main()
    for i in range(0, 10):
        random_delay = int(uniform(1, 15))
        print(f"RUNNING THE {i} ROUND.")
        print(f"Waiting {random_delay} seconds to continue.")
        time.sleep(random_delay)
        cat = choice(list(stock_cats.items()))
        run_stock(cat)
