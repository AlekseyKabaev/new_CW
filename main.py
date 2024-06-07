from src.vacancies import Vacancies
from src.jsonsaver import JsonFile
from src.functions import get_search_query, get_top_n_vacancies, filtered_vacancies, filtered_pay_range


def user_interaction():
    """Функция для взаимодействия с пользователем"""
    search_query = input('Введите поисковый запрос для запроса вакансий из hh.ru: \n')
    vacancies_list = get_search_query(search_query)
    json_saver = JsonFile()
    json_saver.write_vacancies(vacancies_list)
    get_top_n = int(input('Введите количество вакансий для вывода в топ N по зарплате: \n'))
    get_top = get_top_n_vacancies(get_top_n)
    for i in get_top:
        print(Vacancies(**i))
    filter_words = input('Введите ключевые слова для вывода вакансий: \n').lower().split()
    f_v = filtered_vacancies(filter_words)
    for i in f_v:
        print(Vacancies(**i))
    pay_range = input("Введите диапазон зарплат для вывода вакансий: ")  # Пример: 100000 - 150000
    p_r = filtered_pay_range(pay_range)
    for i in p_r:
        print(Vacancies(**i))


if __name__ == "__main__":
    user_interaction()
