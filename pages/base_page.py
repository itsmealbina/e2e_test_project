from pages.locators import base_page_locators

class Base():
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
    
    def open(self, url):
        self.browser.get(url)

    def check_link_name(self):
        text_link = self.browser.find_element(*base_page_locators.link_to_all_products).text
        assert text_link == 'Все товары', 'wrong link name'

    def go_to_all_products(self):
        self.browser.find_element(*base_page_locators.link_to_all_products).click()
