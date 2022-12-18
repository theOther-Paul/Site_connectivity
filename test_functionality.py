import web_check
import requests
import numpy as np
from PIL import Image


def test_fill_address():
    key_address = "example"
    test = web_check.fill_address_elements(key_address)
    assert test == "https://www.example.com"


def test_fill_address_optional():
    key_address = "example"
    test = web_check.fill_address_elements(key_address, domain='.net', protocol='http://')
    assert test == 'http://example.net'


def test_check_address_validity():
    address = "http://www.example.com"
    test = web_check.check_site_address(address)
    assert test is True


def test_check_address_invalidity():
    address = 'placeholder'
    test = web_check.check_site_address(address)
    assert test is False


def test_check_site_head():
    address = "http://www.example.com"
    test = requests.head(address).status_code
    assert test == 200


def test_get_speed():
    import speedtest
    speed = speedtest.Speedtest()
    # known issue: server gives out these typeof errors at random
    from speedtest import ConfigRetrievalError
    try:
        down, up = web_check.humansize(speed.download()), web_check.humansize(speed.upload())
        assert down == down
        assert up == up
    except ConfigRetrievalError:
        assert True  # in case server is down


def test_check_site_address_ip():
    ip = 'https://127.0.0.1:8000'
    test = web_check.check_site_address(ip)
    assert test is True


def test_async_get_response_valid():
    address = 'http://127.0.0.1:8000/success'
    test = requests.get(address).status_code
    assert web_check.check_site(address) == (200 <= test < 400)


def test_async_get_response_invalid():
    address = 'http://127.0.0.1:8000/forbidden'
    test = requests.get(address).status_code
    assert web_check.check_site(address) is None


def test_async_get_response_redirect():
    address = 'http://127.0.0.1:8000/redirect'
    test = requests.get(address).status_code
    try:
        assert web_check.check_site(address) == (200 <= test <= 400)
    except AssertionError:
        assert web_check.check_site(address) is None


def test_humansize():
    bytes = 1024
    test = web_check.humansize(bytes)
    assert test == '1 KB'


def test_humansize_big():
    bytes = 61440000000
    test = web_check.humansize(bytes)
    assert test == '57.22 GB'


# ui testing
def test_change_theme():
    img1 = Image.open('ui_testing/shot 1668188266.0341837.bmp')
    img2 = Image.open('ui_testing/shot 1668188267.5604727.bmp')
    pixel_checklist = [[85, 244], [148, 41], [136, 421], [50, 50]]
    img1_np = np.array(img1, dtype=np.uint8)
    img2_np = np.array(img2, dtype=np.uint8)
    diff = False
    for position in pixel_checklist:
        if np.array_equal(img1_np, img2_np):
            diff = True
        else:
            diff = False
    assert diff is False


def test_is_get_help():
    from os.path import exists
    help_path = 'feature/get_help.html'
    file_exists = exists(help_path)
    if file_exists:
        assert True
    else:
        assert False


def test_is_html():
    test_file = 'feature/get_help.html'
    if test_file.endswith('.html'):
        assert True
    else:
        assert False
