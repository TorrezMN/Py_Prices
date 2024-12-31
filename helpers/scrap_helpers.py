#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created on: 2024-12-16
# Author: Torrez, Milton 



def get_current_date():
    """Returns the current date in the format dd/mm/yy."""
    today = datetime.date.today()
    return f"{today.day}/{today.month}/{today.year % 100}"


def get_current_month_and_year():
    """Returns the current month and year in the format year-month."""
    now = datetime.datetime.now()
    month = now.month
    year = now.year
    return f"{year}-{month:02d}"


def build_and_create_file_route(cat):
    route = os.path.join(BASE_DIR, "data", "fortis",get_current_month_and_year())
    Path(route).mkdir(parents=True, exist_ok=True)
    return Path(route)

