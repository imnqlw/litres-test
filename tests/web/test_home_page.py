import allure
from pages.web.home_page import mp


@allure.label('owner')
@allure.severity('high')
def test_new_book():
    mp.select_new_books()
    mp.check_new_book()


@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
def test_catalog():
    mp.select_catalog()
    mp.check_catalog()


@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
def test_check_book():
    mp.select_found_book()
    mp.check_found_book()


@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
def test_search():
    mp.search_with_filtres()
    mp.check_search()


@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
def test_aa():
    mp.authorisation()
    mp.check_authorisation()
