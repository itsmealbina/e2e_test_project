# from PIL import Image
# import PIL.ImageChops as ich

# img1 = Image.open('screenshots/all_products.png')
# img2 = Image.open('screenshots/preview.png')

# a = ich.difference(image1 = img1, image2 = img2).save('screenshots/res1.jpg')
#b = ich.screen(image1 = img1, image2 = img2).save('screenshots/screen.png')
#c = ich.overlay(image1 = img1, image2 = img2).save('screenshots/overlay.png')


import time

# import sys
# sys.path.append("/Users/albina/Documents/e2e_test_project/")

from pages.base_page import Base

from pathlib import Path
from PIL import Image

base_url = 'http://selenium1py.pythonanywhere.com/ru/'

def test_screenshots(browser,):

    page = Base(browser)
    page.open(base_url)
    page.check_link_name()
    page.go_to_all_products()

    time.sleep(5)