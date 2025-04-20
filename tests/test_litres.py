import allure

from utils.web.home_page import MainPage


@allure.tag("WEB")
@allure.title('Выбор книги')
@allure.epic('книга')
@allure.story('Новая книга')
@allure.feature('Выбор книги')
@allure.label('owner')
@allure.severity('high')
def test_new_book():
    main = MainPage()
    main.select_new_books()
    main.check_new_book()

@allure.title('Проверка каталога')
@allure.epic('Проверка каталога')
@allure.story('Проверка каталога')
@allure.feature('Проверка каталога')
@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
def test_catalog():
    main = MainPage()
    main.select_catalog()
    main.check_catalog()


@allure.title('Проверка книги')
@allure.epic('Проверка книги')
@allure.story('Проверка книги')
@allure.feature('Проверка книги')
@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
def test_check_book():
    main = MainPage()
    main.select_found_book()
    main.check_found_book()


@allure.title('Проверка строки поиска')
@allure.epic('Проверка строки поиска')
@allure.story('Проверка строки поиска')
@allure.feature('Проверка строки поиска')
@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
def test_search():
    main = MainPage()
    main.search_with_filtres()
    main.check_search()
