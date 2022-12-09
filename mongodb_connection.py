from pymongo import MongoClient
  
try:
    conn = MongoClient("mongodb://localhost:27017/")
    print("Connected successfully!!!")
except:  
    print("Could not connect to MongoDB")
  
# database name: mydatabase
db = conn.inteliondb
  
# Created or Switched to collection names: myTable
collection = db.post_api_person
  
# To find() all the entries inside collection name 'myTable'
cursor = collection.find()
for record in cursor:
    print(record)