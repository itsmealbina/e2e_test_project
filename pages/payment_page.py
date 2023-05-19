from pages.base_page import Base
from pages.locators import payment_page_locators


class Payment(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
    
    def is_correct_url(self):
        basket_url = 'http://selenium1py.pythonanywhere.com/ru/checkout/payment-details/'
        current_url = self.browser.current_url
        assert basket_url == current_url, 'wrong url'

    def confirm_payment(self):
        btn = self.browser.find_element(*payment_page_locators.next_button)
        btn.click()