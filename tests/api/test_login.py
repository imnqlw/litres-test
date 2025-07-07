import requests






def test_popular_book():
    response = requests.get("https://www.litres.ru/_next/data/xhgLu5DrzkY2l86qsqBCp/popular.json")
    data = response.json()
    assert data["pageProps"]["_nextI18Next"]["initialI18nStore"]["ru-RU"]["translation"]["Только скидка"] == ('Только скидка')
    assert response.status_code == 200


def test_bonus():
    response = requests.get("https://www.litres.ru/_next/data/xhgLu5DrzkY2l86qsqBCp/landing/litres-bonus-change.json?slug=litres-bonus-change")
    data = response.json()
    assert 'Читайте выгодно в любом формате с программой лояльности Книголов' in data['pageProps']['initialState']
    assert response.status_code == 200


def test_certificate():
    response = requests.get('https://api.litres.ru/foundation/api/auth/socials')
    data = response.json()
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert data["payload"]["data"][0]["provider"] == 'vk'






