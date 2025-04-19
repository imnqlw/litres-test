from utils.web.home_page import MainPage



def test_new_book():
    main = MainPage()
    main.select_new_books()
    main.check_new_book()

def test_catalog():
    main = MainPage()
    main.select_catalog()
    main.check_catalog()

def test_check_book():
    main = MainPage()
    main.select_found_book()
    main.check_found_book()

def test_search():
    main = MainPage()
    main.search_with_filtres()
    main.check_search()




