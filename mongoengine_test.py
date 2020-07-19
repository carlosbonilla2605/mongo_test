from mongoengine import *

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=30)
    last_name = StringField(max_length=30)

class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User)


connect('datacampdb', host='localhost', port=27017)
user = User(email="Connect@derrickmwiti.com", first_name="Derrick", last_name="Mwiti")
user.save()

print(user.id, user.email, user.first_name, user.last_name)
