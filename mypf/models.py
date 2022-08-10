from django.db import models
import pymongo
import urllib
#from django.conf import settings.MDB_OBJ as db_obj
# Create your models here.
def get_Mdb_obj():
    client = pymongo.MongoClient("mongodb+srv://ID:"+urllib.parse.quote('PASSWORD')+"@cluster0.be5tg.mongodb.net/DB_NAME?retryWrites=true&w=majority")
    return client['TEST_DB_1']


#MDB_OBJ = get_Mdb_obj()
# Creating Contact Model
class PersonalAppContact(models.Model):
    name = models.CharField(max_length=196)
    email = models.EmailField()
    subject = models.CharField(max_length=196)
    message = models.TextField()

    def __str__(self):
        return self.email

class MDB_PersonalContact():
    def __init__(self,name,email,subject,message):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message
    def save_data(self):
        db_obj = get_Mdb_obj()
        mycol  =  db_obj['contect_people']
        mydict = { "name": self.name, "email": self.email, 'subject': self.subject, "message": self.message}
        x = mycol.insert_one(mydict)
        self.id = str(x.inserted_id)
        

