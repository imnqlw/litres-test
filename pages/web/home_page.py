import allure
from selene import browser, have


class MainPage:
    @allure.step('Открытие страницы')
    def open(self):
        browser.open('')

    @allure.step('Выбор книги')
    def select_new_books(self):
        browser.open('/')
        browser.element("//a[@class='LowerMenu-module__tITX-W__lowerMenu__item'][contains(text(),'Новинки')]").click()

    @allure.step('Открытие каталога')
    def select_catalog(self):
        browser.open('/')
        browser.element("//button[contains(text(),'Каталог')]").click()

    @allure.step('Поиск книги')
    def select_found_book(self):
        browser.open('/')
        browser.element('[name="q"]').click().type('Python').press_enter()

    @allure.step('Поиск с фильтрами')
    def search_with_filtres(self):
        browser.open('/')
        browser.element('[name="q"]').click().type('Python').press_enter()
        browser.element("//label[contains(text(),'Текст')]").click()

    @allure.step('Проверка книги')
    def check_new_book(self):
        browser.element("//span[@class='PageHeader-module__k0W69G__title__text']").should(have.text('Новинки'))
        return self

    @allure.step('Проверка каталога')
    def check_catalog(self):
        browser.element('[href="/collections/besplatnie-knigi/"]').should(have.text('Бесплатные книги'))

    @allure.step('Проверка книги')
    def check_found_book(self):
        browser.element('[id="pageTitle"]').should(have.text('Python'))

    @allure.step('Проверка поиска книги')
    def check_search(self):
        browser.element('[href="/author/dzheyd-karter/"]').should(have.text('Джейд Картер'))

    @allure.step('Вход в личный кабинет')
    def authorisation(self):
        browser.open('/')
        browser.element('[href="/auth/login"]').click()
        browser.element('[name="email"]').click().type('1hend123456789@gmail.com')
        browser.element(
            "//button[@class='Button-module__QumUZq__button Button-module__QumUZq__button_medium Button-module__QumUZq__button_primary Button-module__QumUZq__button_fullWidth']").click()
        browser.element('[name="pwd"]').click().type('1234qwerty')
        browser.element(
            "//button[@class='Button-module__QumUZq__button Button-module__QumUZq__button_medium Button-module__QumUZq__button_primary Button-module__QumUZq__button_fullWidth']").click()
    @allure.step('Вход выполнен успешно')
    def check_authorisation(self):
        browser.element('.FormHeader-module__shCVMa__header').should(have.text('Добавить номер телефона'))


mp = MainPage()
