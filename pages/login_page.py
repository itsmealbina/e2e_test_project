from pages.base_page import Base
from pages.locators import login_page_locators


class Login(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        
    def is_correct_url(self):
        login_url = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        current_url = self.browser.current_url
        assert login_url == current_url, 'wrong login url'

    def login(self, user, password_value):
        user_name = self.browser.find_element(*login_page_locators.username)
        user_name.send_keys(user)

        password = self.browser.find_element(*login_page_locators.password)
        password.send_keys(password_value)

        confirm_btn = self.browser.find_element(*login_page_locators.login_button)
        confirm_btn.click()

    def is_first_error_message(self):
        info = self.browser.find_element(*login_page_locators.error_message_wrong_data)
        info.is_displayed()
        pattern_text = 'Опаньки! Мы нашли какие-то ошибки - пожалуйста, проверьте сообщения об ошибках ниже и попробуйте еще раз'
        assert info.text == pattern_text, 'wrong text for 1st error message'

    def is_second_error_message(self):
        message = self.browser.find_element(*login_page_locators.error_message_input_correct)
        message.is_displayed()
        pattern_text = 'Пожалуйста, введите правильные имя пользователя и пароль. Оба поля могут быть чувствительны к регистру.'
        assert message.text == pattern_text, 'wrong text in 2nd error message'

    def password_is_emprty(self):
        field = self.browser.find_element(*login_page_locators.password)
        value = field.get_attribute('value')
        assert value == '', 'password filed wasn\'t empty'
