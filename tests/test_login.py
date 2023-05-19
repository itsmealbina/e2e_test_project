from pages.base_page import Base
from pages.login_page import Login

import time
import json
with open('./testdata/users.json') as data:
    users = json.load(data)


base_url = 'http://selenium1py.pythonanywhere.com/ru/'

user_email = users.get('usual_user').get('username')
correct_password = users.get('usual_user').get('password')
incorrect_password = '1234'

def test_authorize_user_with_valid_data(browser):
    page = Base(browser)
    page.open(base_url)
    page.go_to_login_page()

    auth = Login(browser)
    auth.is_correct_url()
    auth.login(user_email, correct_password)
    page.is_correct_url()
    page.there_is_success_message()
    page.header_for_loggined_user()

def test_logout(browser):
    page = Base(browser)
    page.logout()
    page.is_correct_url()
    page.header_for_guest_user()
    
def test_error_for_login_with_wrong_password(browser):
    page = Base(browser)
    page.open(base_url)
    page.go_to_login_page()

    auth = Login(browser)
    auth.is_correct_url()
    auth.login(user_email, incorrect_password)
    auth.is_correct_url()
    auth.is_first_error_message()
    auth.is_second_error_message()
    auth.password_is_emprty()