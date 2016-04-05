
# coding: utf-8

# In[1]:

from pymongo import MongoClient
import pprint


# In[2]:

client=MongoClient("mongodb://localhost:27017")
db=client.examples


# In[27]:

# Projecting queries
def find():
    query={"manufacturer":"Tesla Motors"}
    projection={"_id":1,"name":1}
    result=db.autos.find(query,projection)
    for res in result:
        pprint.pprint(res)


# In[28]:

find()


# In[ ]:




# In[ ]:



