import urllib
import pymongo
import dns
import datetime
from pymongo import MongoClient

username = "dbUser"
password = input("DB Password: ")

client = MongoClient("mongodb+srv://" + username + ":" + urllib.parse.quote(password) +"@py-mongo-hk.8pjyf.mongodb.net/my_db?retryWrites=true&w=majority",tls=True, tlsAllowInvalidCertificates=True)

print(client.test)
db = client["my_db"]
users = db["users"]

# user1= {"username":"user3","password":"@","favorite_number":445, "hobbies":["game", "pizza", "cooking"]}
# user_id = users.insert_one(user1).inserted_id
# print(user_id)

# Make use of lists with [] to insert multiple entries at once or a csv to batch import
# user_id = users.insert_many(user1)

# Count the number of docs in a collection
filter1 = {"username":"user1"}
sort = [("abc",pymongo.DESCENDING)]
skip = 0
limit = 10
doc_count = users.count_documents(filter1, skip=skip)
results = users.find(filter1).sort(sort).skip(skip).limit(limit)
print(doc_count)

# Date time and Keywords
current_date = datetime.datetime.now()
print(current_date)
old_date = datetime.datetime(2009, 8, 11)
uid = users.insert_one({"username":"file","date":current_date})
filter2 = {"$gte":"old_date"}
results = users.find(filter2).sort(sort).skip(skip).limit(limit)

# Indexing and Scaling
db.users.create_index([{"username", pymongo.ASCENDING}])