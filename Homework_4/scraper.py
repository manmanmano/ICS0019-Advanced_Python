"""
Creating a Scraper that grabs from computer page title, price, and picture.
Can be run with: scrapy runspider -o scraper.json scraper.py

"""

import scrapy


class OrdiSetLaptops(scrapy.Spider):
    name = "ordi_laptops" # just a name for the spider
    url = "https://ordi.eu/sulearvutid"
    # set the headers here
    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0' 
    }


    def start_requests(self):
        yield scrapy.http.Request(self.url, headers=self.headers)


    def parse(self, response):
        selectors = ['.item first', '.item', '.item last']
        for selector in selectors:
            SET_SELECTOR = selector
            for chipset in response.css(SET_SELECTOR):
                TITLE_SELECTOR = 'a::text'
                PRICE_SELECTOR = 'span::text'
                IMAGE_SELECTOR = 'img::attr(src)'
                yield {
                        'title': chipset.css(TITLE_SELECTOR).extract_first(),
                        'price': chipset.css(PRICE_SELECTOR).extract_first(),
                        'image': chipset.css(IMAGE_SELECTOR).extract_first(),
                }
