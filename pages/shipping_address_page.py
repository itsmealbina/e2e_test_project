from pages.base_page import Base
from pages.locators import checkout_address_locators
from selenium.webdriver.support.select import Select

import json

with open('./testdata/delivery.json') as addresses:
        data = json.load(addresses)

class Shipping_address(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
    
    def is_correct_url(self):
        basket_url = 'http://selenium1py.pythonanywhere.com/ru/checkout/shipping-address/'
        current_url = self.browser.current_url
        assert basket_url == current_url, 'wrong url'

    def fill_in_shipping_data(self):
        name = data.get('existing_user').get('name')
        surname = data.get('existing_user').get('surname')
        line1 = data.get('existing_user').get('first_line_address')
        city = data.get('existing_user').get('city')
        country = data.get('existing_user').get('country')
        postcode = data.get('existing_user').get('postcode')

        name_field = self.browser.find_element(*checkout_address_locators.name)
        name_field.send_keys(name)

        surname_field = self.browser.find_element(*checkout_address_locators.surname)
        surname_field.send_keys(surname)

        first_line_address_filed = self.browser.find_element(*checkout_address_locators.first_line_address)
        first_line_address_filed.send_keys(line1)

        city_field = self.browser.find_element(*checkout_address_locators.city)
        city_field.send_keys(city)

        postcode_field = self.browser.find_element(*checkout_address_locators.postcode)
        postcode_field.send_keys(postcode)

        # выбор страны из выпадающего списка
        country_field = self.browser.find_element(*checkout_address_locators.country)
        dropdown = Select(country_field)
        dropdown.select_by_visible_text(country)

    def go_to_next_step(self):
        btn = self.browser.find_element(*checkout_address_locators.next_button)
        btn.click()

