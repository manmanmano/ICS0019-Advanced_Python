from bs4 import BeautifulSoup
import requests

# url to search in
start_url = 'https://ordi.eu/sulearvutid'

def parse(start_urls):
    page = requests.get(start_urls)
    soup = BeautifulSoup(page.text, 'html.parser')

    # insert products into list
    chipsets_list = soup.find_all('li', class_ = 'item')
     
    for chip in chipsets_list:
        data = {'Title':'', 'Price':'', 'Picture href':'',}
        data['Title'] = chip.h2.get_text()
        data['Price'] = chip.span.get_text()
        data['Picture href'] = chip.img['src']
        print(data)

    # go to the next page

if __name__ == '__main__':
    parse(start_url)
