import datetime
import csv
import time
import requests
from bs4 import BeautifulSoup
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}


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
    route = os.path.join(BASE_DIR, "data", "super6",get_current_month_and_year())
    Path(route).mkdir(parents=True, exist_ok=True)
    return Path(route)


def get_data(url):
    """Gets page content."""
    response = requests.get(url, headers=headers)
    return response.content


def has_pager(s):
    """Checks if the page has a pager and returns a list of pager values."""

    pager_box = s.find("div", class_="product-pager")
    if pager_box is None:
        return []  # Return an empty list if the pager box is not found

    pager_nums = [element.text for element in pager_box.find_all("a")]
    return [
        int(e) if e.isdigit() else 0 for e in pager_nums if e is not None
    ]  # Handle potential None values


def append_dict_to_csv(file_path, data_dict):
    """Appends a dictionary with specified keys to a CSV file.

    Args:
        file_path (str): The path of the CSV file.
        data_dict (dict): The dictionary containing the data to be appended.

    Returns:
        None
    """

    keys = ["category","prod_name", "prod_price", "product_picture", "run_date"]
    with open(
        Path(file_path, f"super6_data.csv"), "a+", newline=""
    ) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)

        # Write header row only if the file is empty
        if os.path.getsize(Path(file_path,f"super6_data.csv")) == 0:
            writer.writeheader()

        writer.writerow(data_dict)


def process_box(b, c):
    data = {}
    product_title = b.find("a", class_="product-title-link").text
    product_price = "GS." + b.find("span", class_="price-label").text
    product_picture = b.find("a", class_="picture-link").img["src"]
    run_date = get_current_date()
    data["category"]=c
    data["prod_name"] = product_title
    data["prod_price"] = product_price
    data["product_picture"] = product_picture
    data["run_date"] = run_date

    # # Append to file.
    append_dict_to_csv(build_and_create_file_route(c), data)
    print("="*44)
    print("="*44)
    print(c)
    print("="*44)
    print(data)
    print("="*44)


def super6_main(c):
    soup = BeautifulSoup(get_data(c[1]), "html.parser")
    productos = soup.find_all("div", class_="producto")

    try:
        pages = max(has_pager(soup))
    except ValueError as e:
        print(f"Error: {e}")
        # Provide alternative behavior if needed
        print("Using default value instead")
        pages = 0

    for i in productos:
        process_box(i, c[0])


def run_super6(cat):
    super6_main(cat)



