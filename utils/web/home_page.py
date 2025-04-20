import allure
from selene import browser, have


class MainPage:
    @allure.step('Открытие страницы')
    def open(self):
        browser.open('https://www.litres.ru/')

    @allure.step('Выбор книги')
    def select_new_books(self):
        browser.open('https://www.litres.ru/')
        browser.element("//a[@class='LowerMenuV2_lowerMenu__item__KBMA4'][contains(text(),'Новинки')]").click()

    @allure.step('Открытие каталога')
    def select_catalog(self):
        browser.open('https://www.litres.ru/')
        browser.element('[data-testid="header-catalog-button"]').click()

    @allure.step('Поиск книги')
    def select_found_book(self):
        browser.open('https://www.litres.ru/')
        browser.element('.SearchForm_input__qDTKP').click().type('Python').press_enter()

    @allure.step('Поиск с фильтрами')
    def search_with_filtres(self):
        browser.open('https://www.litres.ru/')
        browser.element('.SearchForm_input__qDTKP').click().type('Python').press_enter()
        browser.element("//label[contains(text(),'Русский')]//*[name()='svg']").click()

    @allure.step('Проверка книги')
    def check_new_book(self):
        browser.element("//span[@itemprop='name'][contains(text(),'Новинки')]").should(have.text('Новинки'))
        return self

    @allure.step('Проверка каталога')
    def check_catalog(self):
        browser.element('[href="/collections/besplatnie-knigi/"]').should(have.text('Бесплатные книги'))

    @allure.step('Проверка книги')
    def check_found_book(self):
        browser.element('.SearchTitle_title__Crpui').should(have.text('Python'))

    @allure.step('Проверка поиска книги')
    def check_search(self):
        browser.element('[href="/author/dzheyd-karter/"]').should(have.text('Джейд Картер'))
