import scrapy
from selenium.common.exceptions import NoSuchElementException
import scrapy
import time
from scrapy.http import Request
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BestbuySpider(scrapy.Spider):
    name = "bestbuy"

    # This code is to hide the fact that this is a bot
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) " \
                "Chrome/43.0.2357.130 Safari/537.36 "

    # Enter the bestbuy URL you want to use
    start_urls = [
       "https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659", ]


    def parse(self, response, **kwargs):

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
            if product:
                print("\nFound 1 item to add to cart.\n")

                # Booting WebDriver.
                profile = webdriver.FirefoxProfile(
                    r'C:\Users\Jeric\AppData\Roaming\Mozilla\Firefox\Profiles\gcu59ak7.default-release')
                driver = webdriver.Firefox(profile, executable_path=GeckoDriverManager().install())

                # Starting Webpage.
                driver.get(response.url)
                time.sleep(5)

                # Click Add to Cart.
                print("\nClicking Add To Cart Button.\n")
                driver.find_element_by_xpath(
                    "//*[@class='btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button']").click()
                time.sleep(5)

                # Click Cart.
                print("\nGoing to Shopping Cart.\n")
                driver.get("https://www.bestbuy.com/cart")
                time.sleep(5)

                # Click Check-out Button.
                print("\nClicking Checkout Button.\n")
                driver.find_element_by_xpath("//*[@class='btn btn-lg btn-block btn-primary']").click()

                # Giving Website Time To Login.
                print("\nGiving Website Time To Login..\n")
                wait = WebDriverWait(driver, 20)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH, "//*[@class='btn btn-lg btn-block btn-primary button__fast-track']")))
                time.sleep(3)

               # Giving Website Time To Login.
                print("\nGiving Website Time To Login..\n")
                wait = WebDriverWait(driver, 20)
                wait.until(EC.presence_of_element_located((By.XPATH, "//*[@class='btn btn-lg btn-block btn-primary button__fast-track']")))
                time.sleep(3)

            else:
                print("\nRetrying Bot In 15 Seconds.\n")
                time.sleep(15)
                yield Request(response.url, callback=self.parse, dont_filter=True)