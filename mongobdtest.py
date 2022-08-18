import pymongo
client = pymongo.MongoClient("mongodb+srv://nagesh:Nagesh@cluster0.8pdmvi8.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"sudhanshu",
    "email":"sudhanshu@gmail.com",
    "surname":"kumar"
}
db1 = client['mongobdtest']
coll = db1['test']
coll.insert_one(d)