# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

import json
import requests
from bs4 import BeautifulSoup
import datetime
import time
import ast
from random import randint
from time import sleep



stock_base_url = 'https://www.stock.com.py/default.aspx'


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




def has_href_attribute(anchor_tag):
  """Checks if the given anchor tag (a bs4.element.Tag object) contains the 'href' attribute.

  Args:
    anchor_tag: The bs4.element.Tag object representing the anchor tag to check.

  Returns:
    True if the anchor tag has an 'href' attribute, False otherwise.
  """

  return anchor_tag.has_attr('href')


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
    menu = soup.find_all('div', attrs={"class": "wsmenu-submenu"})
    for i in menu[0].find_all('a'):
        if has_href_attribute(i):
            print(i)
            print('='*33)



if __name__ == "__main__":
    stock_main()

