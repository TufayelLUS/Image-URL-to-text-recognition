import pytesseract
import requests
from PIL.Image import open as imop
import os
import string
from random import choice

# currently available for windows only, try getting the other operating system version of tesseract to use it on other operating system

pytesseract.pytesseract.tesseract_cmd = r'Tesseract\tesseract.exe'


def randStr():
    str_data = string.ascii_letters + string.digits
    my_str = ""
    for i in range(6):
        my_str += choice(str_data)
    return my_str


def imageToText(link):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    }
    print("Downloading image from {}".format(link))
    resp = requests.get(link, headers=headers).content
    image_name = 'temp-{}.png'.format(randStr())
    open(image_name, mode='wb+').write(resp)
    tmp = pytesseract.image_to_string(
        imop(image_name), config='--psm 6 --oem 3')
    os.remove(image_name)
    return tmp


if __name__ == "__main__":
    print(imageToText(
        "https://place image link here"))
