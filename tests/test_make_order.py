from pages.base_page import Base
from pages.all_products_page import All_products_page
from pages.book1_page import Book1
from pages.basket_page import Basket
from pages.checkout_page import Ckeckout_step_1
from pages.shipping_address_page import Shipping_address
from pages.payment_page import Payment
from pages.preview_page import Preview
from pages.confirmation_page import Confirmation

base_url = 'http://selenium1py.pythonanywhere.com/ru/'

def test_buy_product_by_existing_user(browser):
    page = Base(browser)
    page.open(base_url)
    page.check_link_name()
    page.go_to_all_products()

    # проверяем параметры 1й книги
    all_products = All_products_page(browser)
    all_products.is_correct_url()
    all_products.assert_book_name_1()
    all_products.assert_book_price_1()
    all_products.is_correct_image_book_1()
    all_products.check_book_in_stock_1()
    all_products.go_to_book_page()

    #проверяем данные на странице книги
    book_1 = Book1(browser)
    book_1.is_correct_url()
    book_1.assert_book_name()
    book_1.assert_book_price()
    book_1.assert_book_image()
    book_1.assert_book_article()
    book_1.assert_book_product_type()
    book_1.assert_price_without_vat()
    book_1.assert_price_with_vat()
    book_1.assert_tax_value()

    # добавляем книгу в корзину
    book_1.add_book_to_cart()
    book_1.there_is_success_message()
    book_1.there_is_promotion_message()
    book_1.there_is_cart_cost_message()
    
    # переходим в корзину
    book_1.go_to_cart_from_header()

    # страница корзины
    basket = Basket(browser)
    basket.is_correct_url()
    
    basket.check_book_name()
    basket.check_book_price_1_item()
    basket.check_book_price_items()
    basket.check_total_price()
    basket.check_delivery_price()
    basket.check_label_info()

    # переход к оформлению
    basket.go_to_next_step()
    step1 = Ckeckout_step_1(browser)
    step1.is_correct_url()
    step1.fill_in_exist_user_data()
    step1.go_to_next_step()

    address = Shipping_address(browser)
    address.is_correct_url()
    address.fill_in_shipping_data()
    address.go_to_next_step()

    payment = Payment(browser)
    payment.is_correct_url()
    payment.confirm_payment()

    preview = Preview(browser)
    preview.is_correct_url()
    preview.check_info_for_address()
    preview.check_delivery_info()
    preview.check_payment_info()
    preview.check_book_in_list()
    preview.check_total()
    preview.place_order()

    confirm = Confirmation(browser)
    confirm.is_correct_url()
    confirm.check_confirmation_info()
    confirm.check_description_for_confirmation()
    confirm.go_back_to_main_page()

    page.check_link_name()


