
# coding: utf-8

# In[1]:

from pymongo import MongoClient
import pprint


# In[2]:

client=MongoClient("mongodb://localhost:27017")
db=client.examples


# In[23]:

auto=db.autos.find_one({"manufacturer":"Tesla Motors"})


# In[18]:

# updating the document with save()
auto['class']="Premium"
db.autos.save(auto)


# In[24]:

auto


# In[27]:

for a in db.autos.find():
    pprint.pprint(a)


# In[28]:

# updating through update and set
def find():
    auto=db.autos.update({"class":"Premium"},{"$set":{"body-style":"convertible"}})
    auto=db.autos.update({"class":"full-size"},{"$set":{"MoonRoof":"Yes"}})


# In[29]:

find()


# In[31]:

for a in db.autos.find():
    pprint.pprint(a)


# In[32]:

# running unset on the document with class of full size will unset/delete the moonroof field from it
def find():
    auto=db.autos.update({"class":"full-size"},{"$unset":{"MoonRoof":""}})


# In[33]:

find()


# In[34]:

for a in db.autos.find():
    pprint.pprint(a)


# In[35]:

def main():
    db.autos.update({"manufacturer":"Tesla Motors"},
                   {"$set":{"MoonRoof":"Yes"}})


# In[36]:

main()


# In[37]:

for a in db.autos.find():
    pprint.pprint(a)


# In[38]:

#unsetting the moonroof feature 
db.autos.update({"manufacturer":"Tesla Motors"},
               {"$unset":{"MoonRoof":""}})


# In[39]:

for a in db.autos.find():
    pprint.pprint(a)


# In[40]:

#Mutltiupdate
db.autos.update({"manufacturer":"Tesla Motors"},{"$set":{"MoonRoof":"Yes"}},multi=True)


# In[44]:

for a in db.autos.find():
    pprint.pprint(a)
    


# In[45]:

# Removing a document from a collection
db.autos.remove({"class":"full-size"})


# In[46]:

for a in db.autos.find():
    pprint.pprint(a)


# In[47]:

for a in db.myautos.find():
    pprint.pprint(a)


# In[48]:

# drop the entire collection
db.myautos.drop()


# In[50]:

# Hence the entire collection is removed/dropped
for a in db.myautos.find():
    pprint.pprint(a)


# In[ ]:



