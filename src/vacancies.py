class Vacancies:

    def __init__(self, name, url, salary_from, salary_to, employer, snippet):
        self.name = name
        self.url = url
        if salary_from:
            self.salary_from = salary_from
        else:
            self.salary_from = 0
        if salary_to:
            self.salary_to = salary_to
        else:
            self.salary_to = 0
        self.employer = employer
        self.snippet = snippet

    def __str__(self):
        if self.salary_from == 0 and self.salary_to == 0:
            return (f'Название вакансии {self.name}\nНазвание компании {self.employer}\nСсылка на вакансию {self.url}\n'
                    f'Зарплата не указана!\nОписание вакансии: {self.snippet}\n')
        elif self.salary_from == 0:
            return (f'Название вакансии {self.name}\nНазвание компании {self.employer}\nСсылка на вакансию {self.url}\n'
                    f'Зарплата до {self.salary_to}\nОписание вакансии: {self.snippet}\n')
        elif self.salary_to == 0:
            return (f'Название вакансии {self.name}\nНазвание компании {self.employer}\nСсылка на вакансию {self.url}\n'
                    f'Зарплата от {self.salary_from}\nОписание вакансии: {self.snippet}\n')
        else:
            return (f'Название {self.name}\nКомпания {self.employer}\nСсылка на вакансию {self.url}\n'
                    f'Зарплата от {self.salary_from} до {self.salary_to}\nОписание вакансии: {self.snippet}\n')

    def __eq__(self, other):
        """Сравнение ЗП"""
        return self.salary_from == other.salary_from

    def __gt__(self, other):
        """Сравнение ЗП"""
        return self.salary_from > other.salary_from

    def __lt__(self, other):
        """Сравнение ЗП"""
        return self.salary_from < other.salary_from

    @classmethod
    def get_vacancy(cls, data):
        """Получение списка вакансий"""
        list_vacancies = []
        vacancies = data.get("items", [])
        for vacancy in vacancies:
            if vacancy["salary"]:
                list_vacancies.append(cls(vacancy["name"],
                                          vacancy["alternate_url"],
                                          vacancy["salary"]["from"], vacancy["salary"]["to"],
                                          vacancy["employer"]["name"],
                                          vacancy["snippet"]["requirement"]))

            else:
                list_vacancies.append(cls(vacancy["name"],
                                          vacancy["alternate_url"],
                                          0, 0,
                                          vacancy["employer"]["name"],
                                          vacancy["snippet"]["requirement"]))

        return list_vacancies
