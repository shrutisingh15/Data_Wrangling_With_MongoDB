
# coding: utf-8

# In[1]:

from pymongo import MongoClient
import pprint


# In[2]:

client=MongoClient("mongodb://localhost:27017")
db=client.examples


# In[8]:

def find():
    autos = db.autos.find({"manufacturer":"Tesla Motors"})
    for a in autos:
        pprint.pprint(a)


# In[9]:

find()


# In[12]:

def find():
    autos=db.autos.find({"model years":[2013]})
    for a in autos:
        pprint.pprint(a)


# In[13]:

find()


# In[ ]:



