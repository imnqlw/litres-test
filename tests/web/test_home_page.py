import allure
from pages.web.home_page import mp



@allure.epic('Add book to cart')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking book")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_new_book():
    mp.select_new_books()
    mp.check_new_book()



@allure.epic('Add book to cart')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking catalog")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_catalog():
    mp.select_catalog()
    mp.check_catalog()



@allure.epic('Add book to cart')
@allure.label("owner", "flowerfrog")
@allure.feature("Finding book")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_check_book():
    mp.select_found_book()
    mp.check_found_book()



@allure.epic('Add book to cart')
@allure.label("owner", "flowerfrog")
@allure.feature("Searching with filter")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_search():
    mp.search_with_filtres()
    mp.check_search()


@allure.epic('Authorized')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the authorization of the user")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_authorisation(login, passwd):
    mp.authorisation(login, passwd)
    mp.check_authorisation()
