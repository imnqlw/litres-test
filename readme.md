<h1> Проект по тестированию сервиса электронных и аудиокниг "Литрес"</h1>

> <a target="_blank" href="https://www.litres.ru">Ссылка на сайт</a>

![This is an image](design/image/litres_page.png)

<h3> Список проверок, реализованных в автотестах:</h3>

### UI-тесты
- [x] Поиск книги
- [x] Добавление книги в корзину
- [x] Добавление книги в Избранное
- [x] Удаление книги из Избранного

### API-тесты
- [x] Поиск книги
- [x] Добавление книги в корзину
- [x] Проверка каталога с сертификатами

----
### Проект реализован с использованием:
<img src="design/icons/python-original.svg" width="50"> <img src="design/icons/pytest.png" width="50"> <img src="design/icons/intellij_pycharm.png" width="50"> <img src="design/icons/selene.png" width="50"> <img src="design/icons/selenoid.png" width="50"> <img src="design/icons/jenkins.png" width="50"> <img src="design/icons/allure_report.png" width="50"> <img src="design/icons/allure_testops.png" width="50"> <img src="design/icons/tg.png" width="50"> <img src="design/icons/jira.png" width="50">

----
### Локальный запуск
> Для локального запуска с дефолтными значениями необходимо выполнить команду:
```
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install --no-root
pytest tests
```

----
### Удаленный запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/test_litres/">Ссылка на проект в Jenkins</a>


#### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/test_litres/">проект</a>
2. Выбрать пункт `Build with Parameters`
3. Результат запуска сборки можно посмотреть в отчёте Allure

----
### Allure отчет


#### Общие результаты
![This is an image](pic/allure.PNG)
#### Список тест кейсов
![This is an image](pic/case.png)
#### Пример отчета о прохождении ui-теста
![This is an image](pic/example_test_ui_allure.png)
#### Пример отчета о прохождении api-теста
![This is an image](design/image/test_api.png)


## [Видео прохождения автотестов](https://jenkins.autotests.cloud/job/test_litres/38/allure/data/attachments/65715dbcedac12d8.html)
<img title="Selenoid" src="pic/vv.gif"/>
