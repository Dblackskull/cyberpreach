from pymongo import MongoClient
client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')
db = client['Cyberpreach']
collection = db['quiz']
class question():
    def __init__(self,question):
        self.question=collection.find_one({"name":question})
        self.quiz=[]
    def fivequestion(self):
        self.quiz=self.question
        return self.quiz
