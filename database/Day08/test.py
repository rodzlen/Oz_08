# Pymongo
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db =client['example_db']
collection = db['example_collection']

# example_document = {"name":"John", "age":30, "city":"New York"}
# collection.insert_one(example_document)

for doc in collection.find():
    print(doc)

query = {"name":"Jsohn"}
for doc in collection.find(query):
    print(doc)