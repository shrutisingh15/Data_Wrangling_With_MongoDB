
# coding: utf-8

# In[1]:

from pymongo import MongoClient
import pprint


# In[2]:

client=MongoClient("mongodb://localhost:27017")
db=client.examples


# In[3]:

# Computing the no. of documents in myautos collection before inserting any document
num_autos=db.myautos.find().count()


# In[5]:

print "num autos before:",num_autos


# In[6]:

# Creating the cursor to insert all the documents present in autos collection in myautos collection
autos=db.autos.find()


# In[7]:

# Inserting the documents in myautos collection using autos cursor
for a in autos:
    db.myautos.insert(a)


# In[8]:

# Computing the no. of documents in myautos collection after inserting any document
num_autos=db.myautos.find().count()


# In[9]:

print "num autos after:",num_autos


# In[ ]:



