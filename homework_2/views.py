from pymongo import MongoClient


def add_vacancies(some_dict):
    client = MongoClient('localhost', 27017)
    db = client['vacancy_db']
    vacancy_collection = db.vacancy_collection
    vacancy_collection.insert_many(some_dict)

def search_vacancies():
    client = MongoClient('localhost', 27017)
    db = client['vacancy_db']
    collection = db.vacancy_collection
    result = collection.find({salary: /\d/})
    return result