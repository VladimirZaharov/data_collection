from pymongo import MongoClient


class JobparserPipeline(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.vacancy_hhru


    def process_item(self, item, spider):
        collection = self.mongobase[spider.name]
        collection.insert_one(item)

        print(item['salary'])

        return item
