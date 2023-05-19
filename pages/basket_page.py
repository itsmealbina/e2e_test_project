import json

from pages.base_page import Base
from pages.locators import basket_page_locators

with open('./testdata/books.json') as books_array:
        data = json.load(books_array)

class Basket(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def is_correct_url(self):
        basket_url = 'http://selenium1py.pythonanywhere.com/ru/basket/'
        current_url = self.browser.current_url
        assert basket_url == current_url, 'wrong url'

    def check_book_name(self):
         book_name = self.browser.find_element(*basket_page_locators.book_name1).text
         assert book_name == data.get('book1').get('name'), 'wrong book name'

    def check_book_price_1_item(self):
         book_price = self.browser.find_element(*basket_page_locators.price_for_one_item).text
         assert book_price == data.get('book1').get('price'), 'wrong book price for 1 item'

    def check_book_price_items(self):
         book_price = self.browser.find_element(*basket_page_locators.total_price_for_item).text
         assert book_price == data.get('book1').get('price'), 'wrong book price for 1 book all items'

    def check_total_price(self):
        total_basket_price = self.browser.find_element(*basket_page_locators.total_price).text
        assert total_basket_price == data.get('book1').get('price'), 'wrong total price'

    def check_delivery_price(self):
        total_delivery_price = self.browser.find_element(*basket_page_locators.delivery_price).text
        assert total_delivery_price == "0,00 £", 'wrong delivery price'

    def check_label_info(self):
         label_text = self.browser.find_element(*basket_page_locators.promo_message_label).text
         assert label_text == 'Deferred benefit offer', 'wrong label text'

         label_description = self.browser.find_element(*basket_page_locators.description_promo_label).text
         assert label_description == 'You will have your name changed to Barry!', 'wrong label description'

    def go_to_next_step(self):
         btn = self.browser.find_element(*basket_page_locators.go_to_next_step_button)
         btn.click()

         
    