from pages.header import Header
from pages.main_page import Main
from pages.amazon_fashion_header import AmazonFashionHeader
from pages.product_page import ProductPage
from pages.search_results_page import SearchResults



class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = Main(self.driver)
        self.header = Header(self.driver)
        self.amazon_fashion_header = AmazonFashionHeader(self.driver)
        self.product_page = ProductPage(self.driver)
        self.search_results_page = SearchResults(self.driver)
