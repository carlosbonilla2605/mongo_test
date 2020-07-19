from pymongo import MongoClient
from bson.objectid import ObjectId


client = MongoClient()

#client = Mongoclient("localhost", 27017)  # specify host and port
#client = Mongoclient('mongodb://localhost:27017/')  # URI based


db = client['datacampdb']  # new database


# First document insertion
article = {"author": "Derrick Mwiti",
           "about": "Introduction to MongoDB and Python",
           "tags":
                ["mongodb", "python", "pymongo"]
           }
articles = db.articles
result = articles.insert_one(article)
print("First artcile key is: {}".format(result.inserted_id))

# Get collections
print(db.list_collection_names())

# Insert multiple documents
article1 = {"author": "Emmanuel Kens",
            "about" : "Knn and Python",
            "tags" :
                ["Knn", "pymongo"]
            }

article2 = {"author": "Daniel Kimeli",
            "about": "Web Development and Python",
            "tags":
                ["web", "design", "HTML"]
            }

new_articles = articles.insert_many([article1, article2])
print("The new article IDs are {}".format(new_articles.inserted_ids))

# Retrieving a single document with find_one()
print("First article in collection articles: ", articles.find_one())

# Find all documents in a collection
print("Find all documents in collection articles:")
for article in articles.find():
    print(article)

# Find documents using IDs
print("Find documents using ID")
random_id = "5f14bce62f01a0321ad67679" #  Retrieved manually
document = client.db.collection.find_one({"_id":ObjectId(random_id)})
print(document)

# Return some fields only
print("only return some fields")
for article in articles.find({},{ "_id": 0, "author": 1, "about": 1}):
    print(article)

# Sorting the results
print("Sort the results using sort")
doc = articles.find().sort("author", -1)  # -1 is for descending order
for x in doc:
    print(x)

# Update a document
print("Update one document, Change Derrick Mwiti for John David")
query = { "author": "Derrick Mwiti"}
new_author = { "$set" : { "author": "John David" } }
articles.update_one(query, new_author)

for article in articles.find():
    print(article)

# Limited results
print("Limit the results of the query")
limited_result = articles.find().limit(1)
for x in limited_result:
    print(x)

# Delete Document
print("Delete one document")
db.articles.delete_one({"_id":ObjectId(random_id)})

#Delete Many Documents
#print("Delete many documents")
#delete_articles = articles.delete_many({})
#print(delete_articles.deleted_count, " articles deleted.")

#Drop a collection
#articles.drop()
#print(db.list_collection_names())
