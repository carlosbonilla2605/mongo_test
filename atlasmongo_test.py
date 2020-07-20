from pymongo import MongoClient
from random import randint

#Step 1: Connect to MongoDB
client = MongoClient("mongodb+srv://admin:admin@cluster0.epnyx.mongodb.net/Cluster0?retryWrites=true&w=majority")
db = client.business

# Find one
fivestar = db.reviews.find_one({'rating': 5})
print(fivestar)

#Find all and count
#fivestarcount = db.reviews.find({'rating': 5}).count()
#print(fivestarcount)

#Another way of counting (the not deprecated one)
print(db.reviews.count_documents({'rating': 5}))

#Aggregation framework to sum the ocurrence of each rating across the entire data set
print("The sum of each rating occurrance across all data grouped by rating")
stargroup = db.reviews.aggregate(
    #The Aggregation Pipeline is defined as an array of different operations
    [
        #The first stage is to group data
        { '$group':
              {
                  '_id': "$rating",
                  "count" :
                        { '$sum' :1 }
              }
        },
        #The second stage is to sort data
        {
            '$sort': { "_id":1}
        }
        #Close the array with the ] tag
    ]
)
for group in stargroup:
    print(group)