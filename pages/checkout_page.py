from selenium.webdriver.common.keys import Keys
import json

from pages.base_page import Base
from pages.locators import checkout_step_1_locators

with open('./testdata/users.json') as users:
        creds = json.load(users)

class Ckeckout_step_1(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def is_correct_url(self):
        basket_url = 'http://selenium1py.pythonanywhere.com/ru/checkout/'
        current_url = self.browser.current_url
        assert basket_url == current_url, 'wrong url'

    def fill_in_exist_user_data(self):
        user_email = creds.get('usual_user').get('username')
        password = creds.get('usual_user').get('password')
        
        email_field = self.browser.find_element(*checkout_step_1_locators.email_input)
        email_field.send_keys(user_email)
        # выбор радиобаттона для уже существующего пользователя
        choose_radiobutton = self.browser.find_element(*checkout_step_1_locators.checkbox_existing_user)
        choose_radiobutton.click()

        password_field = self.browser.find_element(*checkout_step_1_locators.password_input)
        password_field.send_keys(password)

    def go_to_next_step(self):
        btn = self.browser.find_element(*checkout_step_1_locators.next_button)
        btn.click()