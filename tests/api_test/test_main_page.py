from pages.api.search_page import sp


def test_main_page(base_api_url):
    sp.test_search_page(base_api_url)

def test_certificate(base_api_url):
    sp.test_certificate(base_api_url)

def test_add_card(base_api_url):
    sp.test_add_book_in_cart(base_api_url)


def test_authorisation(base_api_url):
    sp.test_authorisation(base_api_url)