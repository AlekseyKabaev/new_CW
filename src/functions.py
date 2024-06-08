import json

from src.hh_api import HhAPI
from src.vacancies import Vacancies
from src.jsonsaver import JsonFile
import re

hh_api_1 = HhAPI()
json_list = JsonFile()


def get_search_query(search_query):
    """поисковый запрос вакансии"""
    hh_vacancies = hh_api_1.load_vacancies(search_query)
    vacancies_list = Vacancies.get_vacancy(hh_vacancies)
    return vacancies_list


def get_top_n_vacancies(n):
    """функция получения списка из N вакансий с учетом уровня ЗП"""
    json_dict = json_list.get_info_vacancies()
    sorted_list = sorted(json_dict, key=lambda x: abs(x['salary_to'] - x['salary_from']) if x['salary_to'] == 0 or x[
        'salary_from'] == 0 else x['salary_to'])
    return sorted_list[-n:]


def filtered_vacancies(filter_words):
    """функция получения списка вакансий по указанным ключевым словам запроса"""
    res_list = []
    json_dict = json_list.get_info_vacancies()
    for j in json_dict:
        if j["snippet"] is None:
            continue
        words = re.sub(r'[^\w\s]', '', j["snippet"])
        for i in filter_words:
            if i in words.lower().split() and j not in res_list:
                res_list.append(j)
        return res_list


def filtered_pay_range(pay_range):
    """функция получения списка вакансий в указанном диапазоне ЗП"""
    res_list = []
    json_dict = json_list.get_info_vacancies()
    pay_from, pay_to = map(int, pay_range.split('-'))
    for j in json_dict:
        if pay_from <= j['salary_from'] and j['salary_to'] <= pay_to and j not in res_list:
            res_list.append(j)
    return res_list
