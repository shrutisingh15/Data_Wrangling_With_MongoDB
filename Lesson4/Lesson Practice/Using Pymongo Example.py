
# coding: utf-8

# In[11]:

from pymongo import MongoClient
import pprint


# In[12]:

client=MongoClient('mongodb://localhost:27017/')


# In[13]:


# Creating a document in the form of python dictionaries

tesla_s={
    "manufacturer":"Tesla Motors",
    "class":"full-size",
    "body-style":"5-door liftback",
    "production":[2012,2013],
    "model years":[2013],
    "layout":["Rear-motor","rear-wheel drive"],
    "designer":{
        "firstname":"Franz",
        "surname":"von Holzhausen"
    },
    "assembly":[
        {
            "country":"United States",
            "city":"Fremont",
            "state":"California"
        },
        {
            "country":"The Netherlands",
            "city":"Tilburg"
        }
    ]
    
    
}


# In[14]:

# Obtaining a connection to the examples data base
db=client.examples
# inserting the tesla_s document in the autos collection of the example database
db.autos.insert(tesla_s)


# In[15]:

# print the document just inserted in the above line of code.
# Here two object ids are shows because I inserted the same document twice
for a in db.autos.find():
    pprint.pprint(a)


# In[ ]:



