from abc import ABC, abstractmethod
from src.my_encoder import Encoder
import json


class JsonABC(ABC):

    @abstractmethod
    def write_vacancies(self, vacancy):
        pass

    @abstractmethod
    def get_info_vacancies(self):
        pass

    @abstractmethod
    def del_vacancies(self, vacancy):
        pass


class JsonFile(JsonABC):

    def __init__(self):
        self.filename = 'data_file.json'

    def write_vacancies(self, vacancy):
        """Запись Python объекта в файл"""
        with open(f'data/{self.filename}', 'w', encoding='utf-8') as file1:
            json.dump(vacancy, file1, ensure_ascii=False, indent=3, cls=Encoder)

    def get_info_vacancies(self):
        """Получение данных из файла"""
        with open(f'data/{self.filename}', 'r', encoding='utf-8') as file2:
            return json.load(file2)

    def del_vacancies(self, vacancy):
        """Удаление данных из файла"""
        pass
