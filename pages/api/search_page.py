from utils.api.api_helper import api_request

class SearchPage:

    def test_certificate(self, base_url):
        result = api_request(url=base_url, method='GET', endpoint='auth/socials')
        data = result.json()
        assert result.status_code == 200
        assert result.headers['Content-Type'] == 'application/json'
        assert data["payload"]["data"][0]["provider"] == 'vk'

    def test_search_page(self, base_url):
        result = api_request(url=base_url,
                             endpoint='search?',
                             method='GET',
                             params=({'limit': 1, 'q': 'python', 'types': 'text_book'}))
        assert result.status_code == 200
        assert 'Самое полное руководство по разработке' in result.text

    def test_add_book_in_cart(self, base_url):
        name_book = 'Python. Самое полное руководство по разработке в примерах от сообщества Stack Overflow'
        result = api_request(url=base_url, method='GET', endpoint='arts/70338082/series/arts?')
        assert result.status_code == 200
        assert result.headers['Content-Type'] == 'application/json'
        assert name_book in result.text



sp=SearchPage()