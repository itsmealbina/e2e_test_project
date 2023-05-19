def authorize(self, user, user_password):
        user_name = self.browser.find_element(*authorization_page_locators.usrername)
        user_name.send_keys(user)

        password = self.browser.find_element(*authorization_page_locators.password)
        password.send_keys(user_password)

        confirm = self.browser.find_element(*authorization_page_locators.confirm_button)
        confirm.click()