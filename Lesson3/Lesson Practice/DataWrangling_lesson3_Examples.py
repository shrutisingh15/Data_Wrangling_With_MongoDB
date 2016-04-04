
# coding: utf-8

# In[35]:

import csv
import pprint
import math


# In[11]:

# Checking a particular field in a csv file
path='C:/Users/USER/Downloads/autos.csv/Users/gundega/Desktop/github/ud032/Lesson_4/Examples'
filename=(path+'/autos.csv')

'''
The following line of code does data cleaning.
The task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in the range as described above,
  write that line to the output_good file
- if the value of the field is not a valid year as described above, 
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

'''

good_data=[]
bad_data=[]
output_good='output_good.csv'
output_bad='output_bad.csv'

with open(filename,'rb') as f:
    reader=csv.DictReader(f)
    header=reader.fieldnames
    for row in reader:
        if row['URI'].find('dbpedia.org')<0:
            continue
        psy=row['productionStartYear'][:4]
        try:
            psy=int(psy)
            row['productionStartYear']=psy
            if (psy>=1886 and psy <=2014):
                good_data.append(row)
            else:
                bad_data.append(row)
        except:
            if psy == 'NULL':
                bad_data.append(row)

with open(output_good,'w') as good:
    writer=csv.DictWriter(good,delimiter=',',fieldnames=header)
    writer.writeheader()
    for row in good_data:
        writer.writerow(row)
        
with open(output_bad,'w') as bad:
    writer=csv.DictWriter(bad,delimiter=',',fieldnames=header)
    writer.writeheader()
    for row in bad_data:
        writer.writerow(row)


# In[37]:

# check the validity of cross field 
path='C:/Users/USER/Downloads/cities.csv/Users/gundega/Desktop/github/ud032/Lesson_4/Examples'
filename=(path+'/cities.csv')

def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
def check_float(num):
    if is_float(num):
        return float(num)
    
with open(filename,'rb')as f:
    reader=csv.DictReader(f)
    header=reader.fieldnames
    for row in reader:
        population=check_float(row['populationTotal'])
        area=check_float(row['areaLand'])
        populationdensity=check_float(row['populationDensity'])
        if population and area and populationdensity:
            calc_density=float(population/area)
            if math.fabs(calc_density-populationdensity)>10:
                print "possibly bad population density for :", row['name']


# In[ ]:

# function to skip lines a file
def skip_lines(input,skip)
    for i in range(0,skip)
        next(input)
        
        
        
        
def audit_float_field(num,counts):
    num=num.strip()
    if num == "NULL":
        counts['Nulls']+=1
    elif num == "":
        counts['empties']+=1
    elif is_array(num):
        counts['arrays']+=1
    elif not is_number(num):
        print "Found a non Number:", num
    else:
        num=float(num)
        if not((minval<num) and (maxval>num)):
            print "Value out of range.....",num
        
        
input=csv.DictReader(open(filename,'rb'))
skip_lines(input,3)
counts={"Nulls":0,"empties":0,"arrays":0}
nrows=0
for rows in input:
    audit_float_fields(row[fieldname],counts)
    nrows+=1

print "No. of rows:", nrows
print "Nulls:",counts['Nulls']
print "Empties:",counts["Empties"]
print "Arrays:",counts["arrays"]



    

