
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}

cat_name = 'Velas/Fosforo'
cat_url = 'https://www.stock.com.py/category/950-velasfosforo.aspx'


def get_data():
    """Gets page content."""
    response = requests.get(cat_url, headers=headers)
    return response.content

def has_pager(s):
    pager_box = s.find('div', class_='product-pager')
    pager_nums = [i.text for i in pager_box.find_all('a')]
    print(pager_nums)


def stock_main():
    soup = BeautifulSoup(get_data(), "html.parser")
    has_pager(soup)




if __name__ == "__main__":
    stock_main()
