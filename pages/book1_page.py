import json

from pages.base_page import Base
from pages.locators import book1_page

with open('./testdata/books.json') as books_array:
        data = json.load(books_array)

class Book1(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # header
    def go_to_cart_from_header(self):
        btn = self.browser.find_element(*book1_page.see_cart_btn_in_header)
        btn.click()

    # content page
    def is_correct_url(self):
        book1_url = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
        current_url = self.browser.current_url
        assert book1_url == current_url, 'Wrong url'

    def assert_book_name(self):
        book_name = self.browser.find_element(*book1_page.book_name).text
        assert book_name == data.get('book1').get('name'), 'wrong book name'

    def assert_book_price(self):
        book_price = self.browser.find_element(*book1_page.book_price).text
        assert book_price == data.get('book1').get('price'), 'wrong book price'

    def assert_book_image(self):
        book_image = self.browser.find_element(*book1_page.book_image).get_attribute('src')
        assert book_image == data.get('book1').get('img_src_full'), 'wrong image url for book'

    def assert_book_article(self):
        book_article = self.browser.find_element(*book1_page.artikul).text
        assert book_article == data.get('book1').get('article'), 'wrong article'

    def assert_book_product_type(self):
        product_type_on_page = self.browser.find_element(*book1_page.type_product).text
        assert product_type_on_page == data.get('book1').get('product_type'), 'wrong product type'

    def assert_price_without_vat(self):
        price_without_vat_on_page = self.browser.find_element(*book1_page.price_without_vat).text
        assert price_without_vat_on_page == data.get('book1').get('price_without_vat'), 'wrong price without vat'

    def assert_price_with_vat(self):
        price_with_vat_on_page = self.browser.find_element(*book1_page.price_with_vat).text
        assert price_with_vat_on_page == data.get('book1').get('price_with_vat'), 'wrong price with vat'

    def assert_tax_value(self):
        tax_on_page = self.browser.find_element(*book1_page.tax).text
        assert tax_on_page == data.get('book1').get('tax'), 'wrong tax value'

    def add_book_to_cart(self):
        btn = self.browser.find_element(*book1_page.add_to_cart_btn)
        btn.click()

    def there_is_success_message(self):
        label = self.browser.find_element(*book1_page.add_to_cart_label)
        label.is_displayed()
        pattern_str = data.get('book1').get('name') + ' был добавлен в вашу корзину.'
        message_in_label = self.browser.find_element(*book1_page.add_to_cart_message)
        assert pattern_str == message_in_label.text, 'different "add to cart" message'
        
    def there_is_promotion_message(self):
        label = self.browser.find_element(*book1_page.promo_label)
        label.is_displayed()
        str = 'Ваша корзина удовлетворяет условиям предложения Deferred benefit offer.'
        message_in_label = self.browser.find_element(*book1_page.promo_message)
        assert str == message_in_label.text, 'different promo messages'

    def there_is_cart_cost_message(self):
        label = self.browser.find_element(*book1_page.cart_cost_label)
        label.is_displayed()
        pattern_str = 'Стоимость корзины теперь составляет ' + data.get('book1').get('price')
        message_in_label = self.browser.find_element(*book1_page.cart_cost_message).text
        assert message_in_label == pattern_str, 'Wrong message about cart cost'
