from src.vacancies import Vacancies
import json


class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Vacancies):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)
