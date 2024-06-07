import requests
from abc import ABC, abstractmethod


class ABCApi(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class HhAPI(ABCApi):
    """класс, наследующийся от абстрактного класса, для работы с платформой hh.ru"""
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def load_vacancies(self, keyword):
        """функция дял получения вакансий с сайтаhttps://api.hh.ru/vacancies"""
        params = {
            "text": keyword,
            "area": 1,  # Зона запроса вакансии, в нашем случае 1 - Москва
            "page": 0,
            "per_page": 50,  # Количество вакансий на странице
        }

        response = requests.get(self.url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return f'Запрос не выполнен с кодом состояния: {response.status_code}'
