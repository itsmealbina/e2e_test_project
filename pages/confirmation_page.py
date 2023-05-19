from pages.base_page import Base
from pages.locators import confirmation_page_locators

class Confirmation(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
    
    def is_correct_url(self):
        confirmation_page_url = 'http://selenium1py.pythonanywhere.com/ru/checkout/thank-you/'
        current_url = self.browser.current_url
        # print(current_url)
        assert confirmation_page_url == current_url, 'wrong url'

    def check_confirmation_info(self):
        confirm_text = self.browser.find_element(*confirmation_page_locators.header_text).text
        if 'Подтверждение заказа' in confirm_text:
            return True
        else:
            return 'error in header confirmation'
    
    def check_description_for_confirmation(self):
        confirm_text = self.browser.find_element(*confirmation_page_locators.header_text).text
        order_number = confirm_text.split()[-1] # получаем номер заказа как последнее слово из предложения
        my_str = 'Ваш заказ был размещен и выслано сообщение с подтверждением - номер вашего заказа ' + \
            order_number + \
            '. Пожалуйста, скопируйте содержимое этой страницы или распечатайте её для обращений к нам, связанных с этим заказом.'
        description_on_page = self.browser.find_element(*confirmation_page_locators.confirmation_message).text
        assert my_str == description_on_page, 'wrong confiramtion description'

    def go_back_to_main_page(self):
        btn = self.browser.find_element(*confirmation_page_locators.continue_shopping_button)
        btn.click()