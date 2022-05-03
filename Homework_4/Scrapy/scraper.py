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
        """
        In order to crawl and scrape through the page, we use css selectors, as
        it is an easier option. Selectors are three, taken from the list selectors.
        I_SELECTOR is the selector taken from the list each loop, changes every round.
        """
        selectors = ['.item first', '.item', '.item last']
        for selector in selectors:
            I_SELECTOR = selector
            for chipset in response.css(I_SELECTOR):
                TITLE_SELECTOR = 'a::text'
                PRICE_SELECTOR = 'span::text'
                IMAGE_SELECTOR = 'img::attr(src)'
                yield {
                        'Title': chipset.css(TITLE_SELECTOR).extract_first(),
                        'Price': chipset.css(PRICE_SELECTOR).extract_first(),
                        'Picture href': chipset.css(IMAGE_SELECTOR).extract_first(),
                }
            # define a selector for the next page link
            NEXT_PAGE_SELECTOR = '.next::attr(href)'
            # extract the first match and check existance
            next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            if next_page:
                url = response.urljoin(next_page)
                yield scrapy.Request(url, self.parse, headers=self.headers)
