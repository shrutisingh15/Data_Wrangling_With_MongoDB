
# coding: utf-8

# In[1]:

from pymongo import MongoClient
import pprint


# In[2]:

client=MongoClient("mongodb://localhost:27017")
db=client.examples


# In[5]:

# Creating range queries using $gt and $lt operators . It will return all the cities where population is in the range
def find():
    query={"population":{"$gt":250000,"$lt":500000}}
    cities_result=db.cities.find(query)
    
    num_cities=0
    for c in cities_result:
        pprint.pprint(c)
        num_cities+=1
        
    print "No. of cities matching : %d" %num_cities


# In[7]:

# Finding all the cities where city names begin with X
def find():
    query={"name":{"$gte": "X"}}
    result=db.cities.find(query)
    num_cities=0
    for r in result:
        pprint.pprint(r)
        num_cities+=1
       
    
    print "No. of cities matching:%d" %num_cities


# In[8]:

# find cities with founding date in the range
def find():
    query={"foundingDate":
           {"$gte":datetime(1837,1,1),"$lte":datetime(1837,12,31)}
          }
    result=db.cities.find(query)
    num_cities=0
    for r in result:
        pprint.pprint(r)
        num_cities+=1
        
    print "No. of cities matching:%d" %num_cities


# In[10]:

# finding cities where country is not United States
def find():
    query={"country":{"$ne":"United States"}}
    result=db.cities.find(query)
    num_cities=0
    for r in result:
        pprint.pprint(r)
        num_cities+=1
    
    print "No. of cities matching:%d" %num_cities


# In[13]:

# exists operator
query={"governmentType":{"$exists":1}}
db.cities.find(query).count()   # it will return no. of the cities where the field governmentType exists

query={"governmentType":{"$exists":0}}  # without governmentType
db.cities.find(query).count()

# Lets take a look at one of those documents where governmentType field exists
db.cities.find(query).pretty()


# In[15]:

# lets use regular expression queries to match strings
query={"motto":{"$regex":"friendship"}}
db.cities.find(query).pretty()

query={"motto":{"$regex":"[Ff]rienship"}}
db.cities.find(query).pretty()

query={"motto":{"$regex":"[Ff]riendship|[Hh]appiness|[Pp]ride"}}
db.cities.find(query)


# In[ ]:

# using $in operator
db.cities.find({"model years":1980}).pretty()
db.cities.find({"model years":{"$in":[1965,1966,1967]}}).count()  # the result set must contain any of the single or more values


# In[ ]:

# using $all operator
db.cities.find({"model years":{"$all":[1965,1966,1969,1970]}}).count()  # the result set must contain all the values


# In[ ]:

#using dot notation
db.cities.find({"dimensions.weight":{"$gt":5000}}).count() 



# In[ ]:



