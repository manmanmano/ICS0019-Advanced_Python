"""
In order to get json format this script must be run as follows:

python3 soup.py > soup_output.json !!! UNCOMMENT REQUIRED LINES 11, 31, 43, 45

soup_output.json will contain the list of items.
"""

from bs4 import BeautifulSoup
import requests
# import json

# url to search in
start_url = 'https://ordi.eu/sulearvutid'

def parse(start_urls):
    page = requests.get(start_urls)
    soup = BeautifulSoup(page.text, 'html.parser')

    # insert products into list
    chipsets_list = soup.find_all('li', class_ = 'item')
    
    for chip in chipsets_list:
        data = {"Title":"", "Price":"", "Picture href":"",}
        data["Title"] = chip.h2.get_text()
        data["Price"] = chip.span.get_text()
        data["Picture href"] = chip.img['src']
        # needed to format data to json
        # on output is needed to run certain command
        # last comma in json must be manually deleted
        # print(json.dumps(data) + ",")

    # go to the next page
    try:
        next_page = soup.find('a', class_ = 'next')['href']
        if next_page:
            parse(next_page)
    except:
        return


if __name__ == '__main__':
    # print("[")
    parse(start_url)
    # print("]")
