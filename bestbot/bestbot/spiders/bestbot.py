import scrapy
from selenium.common.exceptions import NoSuchElementException


class Bestbot(scrapy.Spider):
    name = "bestbuy"

    # This code is to hide the fact that this is a bot
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) " \
                "Chrome/43.0.2357.130 Safari/537.36 "

    # Enter the bestbuy URL you want to use
    start_urls = [
       "https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402", ]


    def parse(self, response):

    # Checking if the item is available
        try:
            product = response.xpath(
                "//*[@class='btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button']")
            if product:
               print(f"\nItem is Currently: Available.\n")
            else:
               print("\nItem is Out of Stock.\n")
        except NoSuchElementException:
            pass
