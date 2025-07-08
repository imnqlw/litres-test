from pages.api.search_page import sp
import allure


@allure.epic('API. Authorized')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking main page")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.label('layer', 'api')
@allure.severity('normal')
def test_main_page(base_api_url):
    sp.test_search_page(base_api_url)

@allure.epic('API. Search')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking certificate")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_certificate(base_api_url):
    sp.test_certificate(base_api_url)


@allure.epic('API. Search')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the book search on the main page")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_add_card(base_api_url):
    sp.test_add_book_in_cart(base_api_url)

@allure.epic('API. Authorized')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the authorization of the user")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.label('layer', 'api')
@allure.severity('normal')
def test_authorisation(base_api_url):
    sp.test_authorisation(base_api_url)