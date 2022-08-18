import pymongo
client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.8pdmvi8.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"sudhanshu",
    "email":"sudhanshu@gmail.com",
    "surname":"kumar"
}
db1 = client['main']
coll = db1['test']
coll.insert_one(d)