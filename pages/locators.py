from selenium.webdriver.common.by import By


class base_page_locators():
    login_button = (By.XPATH, '//*[@id="login_link"]')
    hello_message_section = (By.ID, 'messages')
    hello_message_text = (By.XPATH, '//*[@id="messages"]/div/div')
    account_link = (By.XPATH, '//*[@id="top_page"]/div[2]/div/ul/li[1]/a')
    logout_link = (By.ID, 'logout_link')

    link_to_all_products = (By.XPATH, '//*[@id="browse"]/li/ul/li[1]/a')

class all_products_page():
    book_name_1 = (By.XPATH, '//a[@title="The shellcoder\'s handbook"]') # \ для того чтобы учесть кавычку
    book_price_1 = (By.XPATH, '//p[@class="price_color"]')
    book_image_1 = (By.XPATH, '//*[@id="default"]/div[2]/div/div/div/section/div/ol/li[1]/article/div[1]/a/img')
    book_in_stock_1 = (By.XPATH, '//*[@id="default"]/div[2]/div/div/div/section/div/ol/li[1]/article/div[2]/p[2]')
    add_to_cart_button_for_book_1 = (By.XPATH, '//*[@id="default"]/div[2]/div/div/div/section/div/ol/li[1]/article/div[2]/form/button')

class book1_page():
    book_name = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    book_price = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    book_image = (By.XPATH, '//*[@id="product_gallery"]/div/div/div/img')
    add_to_cart_btn = (By.XPATH, '//*[@id="add_to_basket_form"]/button')

    artikul = (By.XPATH, '//*[@id="content_inner"]/article/table/tbody/tr[1]/td')
    type_product = (By.XPATH, '//*[@id="content_inner"]/article/table/tbody/tr[2]/td')
    price_without_vat = (By.XPATH, '//*[@id="content_inner"]/article/table/tbody/tr[3]/td')
    price_with_vat = (By.XPATH, '//*[@id="content_inner"]/article/table/tbody/tr[4]/td')
    tax = (By.XPATH, '//*[@id="content_inner"]/article/table/tbody/tr[5]/td')

    add_to_cart_label = (By.XPATH, '//*[@id="messages"]/div[1]')
    add_to_cart_message = (By.XPATH, '//*[@id="messages"]/div[1]/div')

    promo_label = (By.XPATH, '//*[@id="messages"]/div[2]')
    promo_message = (By.XPATH, '//*[@id="messages"]/div[2]/div')

    cart_cost_label = (By.XPATH, '//*[@id="messages"]/div[3]')
    cart_cost_message = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]')

    see_cart_btn = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[2]/a[1]')
    checkout_btn = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[2]/a[2]')

    see_cart_btn_in_header = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')


class basket_page_locators():
    book_name1 = (By.XPATH, '//*[@id="basket_formset"]/div/div/div[2]/h3/a')
    price_for_one_item = (By.XPATH, '//*[@id="basket_formset"]/div/div/div[4]/p')
    total_price_for_item = (By.XPATH, '//*[@id="basket_formset"]/div/div/div[5]/p')

    # total info
    total_price = (By.XPATH, '//*[@id="basket_totals"]/table/tbody/tr[2]/th[2]')
    delivery_price = (By.XPATH, '//*[@id="basket_totals"]/table/tbody/tr[5]/th[2]')
    promo_message_label = (By.XPATH, '//*[@id="basket_totals"]/table/tbody/tr[8]/td/span')
    description_promo_label = (By.XPATH, '//*[@id="basket_totals"]/table/tbody/tr[8]/td/p')
    go_to_next_step_button = (By.XPATH, '//*[@id="content_inner"]/div[3]/div/div/a')

class checkout_step_1_locators():
    email_input = (By.XPATH, '//*[@id="id_username"]')
    checkbox_existing_user = (By.XPATH, '//*[@id="id_options_2"]')
    password_input = (By.XPATH, '//*[@id="id_password"]')
    next_button = (By.XPATH, '//*[@id="default"]/div/div/form/div[5]/div/div/button')

class checkout_address_locators():
    header_address = (By.TAG_NAME, 'h1')
    name = (By.XPATH, '//input[@name="first_name"]')
    surname = (By.XPATH, '//input[@name="last_name"]')
    first_line_address = (By.XPATH, '//input[@name="line1"]')
    city = (By.XPATH, '//input[@name="line4"]')
    postcode = (By.XPATH, '//input[@name="postcode"]')
    country = (By.XPATH, '//*[@id="id_country"]')
    next_button = (By.XPATH, '//*[@id="new_shipping_address"]/div[13]/div/button')

class payment_page_locators():
    next_button = (By.XPATH, '//*[@id="view_preview"]')

class preview_page_locators():
    header = (By.TAG_NAME, 'h1')
    # блок с адресом
    address_name = (By.XPATH, '//*[@id="default"]/div/div/div[3]/div[1]/div[2]/h3')
    change_address_link = (By.XPATH, '//*[@id="default"]/div/div/div[3]/div[1]/div[2]/a')
    name_and_surname = (By.XPATH, '//*[@id="default"]/div/div/div[3]/div[1]/div[2]/address/text()[1]')
    first_line_address = (By.XPATH, '//*[@id="default"]/div/div/div[3]/div[1]/div[2]/address/text()[2]')
    city = (By.XPATH, '//*[@id="default"]/div/div/div[3]/div[1]/div[2]/address/text()[3]')
    postcode = (By.XPATH, '//*[@id="default"]/div/div/div[3]/div[1]/div[2]/address/text()[4]')
    country = (By.XPATH, '//*[@id="default"]/div/div/div[3]/div[1]/div[2]/address/text()[5]')
    full_address = (By.XPATH, '//*[@id="default"]/div/div/div[3]/div[1]/div[2]/address')

    # блок доставки
    delivery_name = (By.XPATH, '//*[@id="default"]/div/div/div[3]/div[1]/div[3]/h3')
    delivery_change_link = (By.XPATH, '//*[@id="default"]/div/div/div[3]/div[1]/div[3]/a')
    text_for_delivery = (By.XPATH, '//*[@id="default"]/div/div/div[3]/div[1]/div[3]/p')

    # блок оплаты
    payment_name = (By.XPATH, '//*[@id="default"]/div/div/div[3]/div[2]/div[2]/h3')
    change_payment_link = (By.XPATH, '//*[@id="default"]/div/div/div[3]/div[2]/div[2]/a')

    # блок с составом заказа
    name_order_list = (By.XPATH, '//*[@id="default"]/div/div/div[4]/h2')
    item_name = (By.XPATH, '//*[@id="default"]/div/div/div[6]/div/div[2]/h3/a')
    item_quantity = (By.XPATH, '//*[@id="default"]/div/div/div[6]/div/div[3]')
    total_item_price = (By.XPATH, '//*[@id="default"]/div/div/div[6]/div/div[4]/p')

    # блок всего
    total_name = (By.XPATH, '//*[@id="default"]/div/div/div[7]/div[2]/div[1]/h2')
    total_in_basket_price = (By.XPATH, '//*[@id="basket_totals"]/table/tbody/tr[2]/th[2]')
    free_delivery_price = (By.XPATH, '//*[@id="basket_totals"]/table/tbody/tr[5]/th[2]')
    actions_after_order_name = (By.XPATH, '//*[@id="basket_totals"]/table/tbody/tr[7]/th/h3')
    label_name = (By.XPATH, '//*[@id="basket_totals"]/table/tbody/tr[8]/td/span')
    label_description = (By.XPATH, '//*[@id="basket_totals"]/table/tbody/tr[8]/td/p')

    total_price = (By.XPATH, '//*[@id="basket_totals"]/table/tbody/tr[10]/td/h3')
    place_order_button = (By.ID, 'place-order')
    
class confirmation_page_locators():
    header_text = (By.TAG_NAME, 'h1')
    confirmation_message = (By.XPATH, '//*[@id="default"]/div/div/p')
    continue_shopping_button = (By.XPATH, '//*[@id="default"]/div/div/div[8]/div/div[2]/p/a')

class login_page_locators():
    username = (By.XPATH, '//input[@name="login-username"]')
    password = (By.XPATH, '//input[@name="login-password"]')
    login_button = (By.NAME, 'login_submit')
    error_message_wrong_data = (By.XPATH, '//*[@id="login_form"]/div[1]')
    error_message_input_correct = (By.XPATH, '//*[@id="login_form"]/div[2]')
   

