from bs4 import BeautifulSoup
import requests

# url to search in
start_url = 'https://ordi.eu/sulearvutid'

def parse(start_urls):
    page = requests.get(start_url)
    soup = BeautifulSoup(page.text, 'html.parser')

    # insert products into list
    selectors = ['item first', 'item', 'item last']
    chipsets_list = []
    for selector in selectors:
        chipsets_list = soup.find_all("li", class_ = selector)
     
    for chip in chipsets_list:
        data = {'title':'', 'price':'', 'image':'',}
        data['title'] = chip.a.get_text()
        data['price'] = chip.span.get_text()
        data['image'] = chip.img['href']
        print(data)
