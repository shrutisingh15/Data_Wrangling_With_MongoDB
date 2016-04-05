
# coding: utf-8

# In[1]:

from pymongo import MongoClient
import pprint


# In[2]:

client=MongoClient("mongodb://localhost:27017")
db=client.examples


# In[5]:

def find():
    result=db.autos.find({"manufacturer":"Tesla Motors","class":"full-size"})
    for r in result:
        pprint.pprint(r)


# In[6]:

find()


# In[ ]:



