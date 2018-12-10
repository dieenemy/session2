from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)

db = client.get_database()

post_connection = db["customers"]

new_document = {
    "title": "Flat world",
    "author": "Trần Tùng",
    "content": "There are different opinions on knowledge so- ciety and on globalization, but we will deal in this paper with Thomas Friedman's flat world. ",
}

post_connection.insert_one(new_document)

client.close()