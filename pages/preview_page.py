from pages.base_page import Base
from pages.locators import preview_page_locators

import json
with open('./testdata/delivery.json') as delivery:
    data = json.load(delivery)

with open('./testdata/books.json') as book:
     item = json.load(book)


class Preview(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
    
    def is_correct_url(self):
        basket_url = 'http://selenium1py.pythonanywhere.com/ru/checkout/preview/'
        current_url = self.browser.current_url
        assert basket_url == current_url, 'wrong url'

    def check_info_for_address(self):
        view_order = self.browser.find_element(*preview_page_locators.header).text
        assert view_order == 'Просмотреть заказ', 'wrong header name'

        address_header = self.browser.find_element(*preview_page_locators.address_name).text
        assert address_header == 'Адрес', 'wrong text for address'

        there_is_change_link = self.browser.find_element(*preview_page_locators.change_address_link)
        there_is_change_link.is_displayed()

        full_address = self.browser.find_element(*preview_page_locators.full_address).text
        my_str =  data.get('existing_user').get('name') + ' ' + data.get('existing_user').get('surname') + '\n'\
         + data.get('existing_user').get('first_line_address') + '\n' + data.get('existing_user').get('city') + \
            '\n' + data.get('existing_user').get('postcode') + '\n' + data.get('existing_user').get('country')
        assert full_address == my_str, 'wrong shipping details'

    def check_payment_info(self):
        payment_text = self.browser.find_element(*preview_page_locators.payment_name).text
        assert payment_text == 'Оплата', 'wrong payment text'

        change_payment_link = self.browser.find_element(*preview_page_locators.change_payment_link)
        change_payment_link.is_displayed()

    def check_delivery_info(self):
         delivery_text = self.browser.find_element(*preview_page_locators.delivery_name).text
         assert delivery_text == 'Способ доставки', 'wrong text for delivery'

         free_delivery_text = self.browser.find_element(*preview_page_locators.text_for_delivery).text
         assert free_delivery_text == 'Бесплатная доставка', 'wrong text for free delivery'

         change_delivery_link = self.browser.find_element(*preview_page_locators.delivery_change_link)
         change_delivery_link.is_displayed()

    def check_book_in_list(self):
        section_name = self.browser.find_element(*preview_page_locators.name_order_list).text
        assert section_name == 'Состав заказа', 'wrong header for section'

        bookname = self.browser.find_element(*preview_page_locators.item_name).text
        assert bookname == item.get('book1').get('name'), 'wrong bookname'

        quantity = self.browser.find_element(*preview_page_locators.item_quantity).text
        #print('\n' + quantity + '\n')
        assert quantity == '1', 'wrong quantity'

        total_price_item = self.browser.find_element(*preview_page_locators.total_item_price).text
        #print('total_price_for_item: \n' + total_price_item + '\n')
        assert total_price_item == item.get('book1').get('price')

    def check_total(self):
        section_name = self.browser.find_element(*preview_page_locators.total_name).text
        assert section_name == 'Всего', 'wrong section name'

        total_price_basket = self.browser.find_element(*preview_page_locators.total_in_basket_price).text
        assert total_price_basket == item.get('book1').get('price'), 'wrong total price'

        delivery_price = self.browser.find_element(*preview_page_locators.free_delivery_price).text
        assert delivery_price == item.get('book1').get('tax')

        name_actions = self.browser.find_element(*preview_page_locators.actions_after_order_name).text
        assert name_actions == 'Действия после заказа', 'wrong name section for actions'

        promo_label = self.browser.find_element(*preview_page_locators.label_name).text
        assert promo_label == 'Deferred benefit order'

        promo_message = self.browser.find_element(*preview_page_locators.label_description).text
        assert promo_message == 'You will have your name changed to Barry!'

        total_price = self.browser.find_element(*preview_page_locators.total_price).text
        assert total_price == item.get('book1').get('price'), 'wrong total price including delivery'   
         

    def place_order(self):
        btn = self.browser.find_element(*preview_page_locators.place_order_button)
        btn.click()
