import allure

from utils.web.home_page import MainPage



@allure.label('owner')
@allure.severity('high')
def test_new_book():
    main = MainPage()
    main.select_new_books()
    main.check_new_book()


@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
def test_catalog():
    main = MainPage()
    main.select_catalog()
    main.check_catalog()




@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
def test_check_book():
    main = MainPage()
    main.select_found_book()
    main.check_found_book()



@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
def test_search():
    main = MainPage()
    main.search_with_filtres()
    main.check_search()
