# from selenium.webdriver.common.by import By
import json

from pages.base_page import Base
from pages.locators import all_products_page

with open('./testdata/books.json') as books_array:
        data = json.load(books_array)

class All_products_page(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def is_correct_url(self):
        all_products_url = 'http://selenium1py.pythonanywhere.com/ru/catalogue/'
        current_url = self.browser.current_url
        assert all_products_url == current_url, 'Wrong url'

    def assert_book_name_1(self):
        book_name = self.browser.find_element(*all_products_page.book_name_1).text
        #assert book_name == 'The shellcoder\'s handbook', 'Wrong book name'
        assert book_name == data.get('book1').get('name'), 'Wrong book name'

    def assert_book_price_1(self):
        book_price = self.browser.find_element(*all_products_page.book_price_1).text
        # book_price_value = float((book_price.split('£')[0]).replace(',', '.'))
        assert book_price == data.get('book1').get('price'), 'Wrong book price'

    def is_correct_image_book_1(self):
        book_image_link = self.browser.find_element(*all_products_page.book_image_1).get_attribute('src')
        assert book_image_link == data.get('book1').get('img_src'), 'Wrong image url'

    def check_book_in_stock_1(self):
       label = self.browser.find_element(*all_products_page.book_in_stock_1)
       label.is_displayed()
    
    def go_to_book_page(self):
        link = self.browser.find_element(*all_products_page.book_name_1)
        link.click()
        

# login
# logout
