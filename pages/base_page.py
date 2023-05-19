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
    
    def is_correct_url(self):
        pattern = 'http://selenium1py.pythonanywhere.com/ru/'
        current = self.browser.current_url
        assert pattern == current, 'wrong url for start page'

    def go_to_all_products(self):
        self.browser.find_element(*base_page_locators.link_to_all_products).click()

    def go_to_login_page(self):
        link = self.browser.find_element(*base_page_locators.login_button)
        link.click()

    def there_is_success_message(self):
        section = self.browser.find_element(*base_page_locators.hello_message_section)
        section.is_displayed()
        text = self.browser.find_element(*base_page_locators.hello_message_text).text
        assert text == 'Рады видеть вас снова', 'Wrong text message'

    def header_for_loggined_user(self):
        profile = self.browser.find_element(*base_page_locators.account_link)
        profile.is_displayed()
        assert profile.text == 'Аккаунт', 'wrong text for account link in header'

        logout = self.browser.find_element(*base_page_locators.logout_link)
        logout.is_displayed()
        assert logout.text == 'Выход', 'wrong text for logout link in header'

    def header_for_guest_user(self):
        text_login_link = self.browser.find_element(*base_page_locators.login_button).text
        assert text_login_link == 'Войти или зарегистрироваться', 'wrong text for guest user for login'

    def logout(self):
        logout = self.browser.find_element(*base_page_locators.logout_link)
        logout.click()

