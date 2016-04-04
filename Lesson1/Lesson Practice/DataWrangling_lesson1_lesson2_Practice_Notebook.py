
# coding: utf-8

# In[3]:

Datafile='beatles-diskography.csv'


# In[2]:

#parse a csv file and use strip() to get rid of extraneous white spaces

def parse_file(Datafile):
    data=[]
    with open(Datafile,'rb') as f:
        header=f.readline().split(',')
        counter=0
        for line in f:
            if counter ==2:
                break
            fields = line.split(',')
            entry ={}
            
            for i,value in enumerate(fields):
                entry[header[i].strip()]=value.strip()
           
            data.append(entry)
            counter+=1
    return data    


# In[3]:

parse_file(Datafile)


# In[6]:

import csv
import pprint


# In[5]:

# reading a csv file INTO a dictionary through dictreader class
with open(Datafile,'rb') as sd:
    r=csv.DictReader(sd)
    print list(r)


# In[7]:


'''

def parse_csv(Datafile):
    data=[]
    with open(Datafile,'rb') as sd:
        reader=csv.DictReader(sd)
        for line in reader:
            data.append(line)
            
    return data

'''


def parse_csv(Datafile):
    data=[]
    with open(Datafile,'rb') as sd:
        readerline=csv.reader(sd)
        for l in readerline:
            data.append(l)
    return data        


# In[8]:

d=parse_csv(Datafile)
pprint.pprint(d)


# In[9]:

DataFile='2013_ERCOT_Hourly_Load_Data.xls'


# In[53]:

import xlrd


# In[29]:

def parse_xls(DataFile):
    workbook=xlrd.open_workbook(DataFile)
    sheet=workbook.sheet_by_index(0)
    
    data=[[sheet.cell_value(row,col)
              for col in range(sheet.ncols)]
                  for row in range(sheet.nrows)]
    
    print '\nList Comprehension'
    print 'data[3][2]:',
    print data[3][0]
    


# In[30]:

parse_xls(DataFile)


# In[40]:

w=xlrd.open_workbook(DataFile)
sheet=w.sheet_by_index(0)
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
          if row ==50:
            print sheet.cell_value(row,col)
        


print '\n',sheet.cell_value(3,2)
print sheet.cell_type(3,2)

print sheet.col_values(3,start_rowx=1,end_rowx=4)
print sheet.row_values(3,start_colx=1,end_colx=4)

exceltime=sheet.cell_value(1,0)
print xlrd.xldate_as_tuple(exceltime,0)


# In[66]:

# Slicing a column of an excel file and finding the max and min value in that file and then finding the positions of those max 
# and min values .Then using those positions to find the corresponding time
workbook=xlrd.open_workbook(DataFile)
sheet=workbook.sheet_by_index(0)

sheet_data=[[sheet.cell_value(row,col)
                 for row in range(sheet.nrows)]
                     for col in range(sheet.ncols)]

cv=sheet.col_values(1,start_rowx=1,end_rowx=None)

maxvalue=max(cv)
minvalue=min(cv)

maxpos=cv.index(maxvalue)+1
minpos=cv.index(minvalue)+1

maxtime=sheet.cell_value(maxpos,0)
mintime=sheet.cell_value(minpos,0)

realmaxtime= xlrd.xldate_as_tuple(maxtime,0)
realmintime=xlrd.xldate_as_tuple(mintime,0)

avgcoast=sum(cv)/float(len(cv))


# In[67]:

# Creating a dictionary for the values obtained above
data={
    'maxtime':realmaxtime,
    'maxvalue':maxvalue,
    'mintime':realmintime,
    'minvalue':minvalue,
    'avgcoast':avgcoast
    
}


# In[68]:

pprint.pprint(data)

data


# In[73]:

# Slicing a column of an excel file and finding the max and min value in that file and then finding the positions of those max 
# and min values .Then using those positions to find the corresponding time
def parse_xfile(DataFile):
    workbook=xlrd.open_workbook(DataFile)
    sheet=workbook.sheet_by_index(0)
    cv=sheet.col_values(1,start_rowx=1,end_rowx=None)
    avgcoast=sum(cv)/len(cv)
    
    maxvalue=max(cv)
    minvalue=min(cv)
    maxpos=cv.index(maxvalue)+1
    minpos=cv.index(minvalue)+1
    
    maxtime=sheet.cell_value(maxpos,0)
    mintime=sheet.cell_value(minpos,0)
    
    realmaxtime=xlrd.xldate_as_tuple(maxtime,0)
    realmintime=xlrd.xldate_as_tuple(mintime,0)
    
    data={
        'maxvalue': maxvalue,
        'realmaxtime': realmaxtime,
        'minvalue':minvalue,
        'realmintime':realmintime,
        'avgcoast':avgcoast
    }
    return data


# In[74]:

parse_xfile(DataFile)


# In[77]:

xlfile='2013_ERCOT_Hourly_Load_Data.xls'
filename='2013.csv'
def parse_xlfile(xlfile):
    workbook=xlrd.open_workbook(xlfile)
    sheet=workbook.sheet_by_index(0)
    data={}
    for n in range(1,9):
        cv=sheet.col_values(n,start_rowx=1,end_rowx=None)
        maxvalue=max(cv)
        maxpos=cv.index(maxvalue)+1
        maxtime=sheet.cell_value(maxpos,0)
        realtime=xlrd.xldate_as_tuple(maxtime,0)
        station=sheet.cell_value(0,n)
        data[station]={"maxvalue":maxvalue,
                      "maxitime":realtime}
        
        
    ##print data
    ##
    
    for s in data:
        print data[s]['maxitime']
        
     
    return data

def save_file(data,filename):
    with open(filename,'w') as f:
        w=csv.writer(f,delimiter='|')
        w.writerow(['Station','Year','Month','Day','Hour','Max Load'])
        for s in data:
            year,month,day,hour,_,_=data[s]['maxitime']
            w.writerow([s,year,month,day,hour,data[s]['maxvalue']])

    


# In[78]:

data=parse_xlfile(xlfile)
save_file(data,filename)


# In[89]:

import json
import requests

BASE_URL='http://musicbrainz.org/ws/2'
ARTIST_URL=BASE_URL+'/artist/'

query_type={"simple":{},
           "atr":{"inc":"aliases+tags+ratings"},
           "aliases":{"inc":"aliases"},
           "releases":{"inc":"releases"}}

def query_site(url,params,uid="",fmt="json"):
    params["fmt"]=fmt
    r =requests.get(url+uid,params=params)
    print "requesting",r.url
    if r.status_code==requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()
        
        
def query_by_name(url,params,name):
    params["query"]="artist:" + name
    return query_site(url,params)

def pretty_print(data,indent=4):
    if type(data)==dict:
        print json.dumps(data,indent=indent,sort_keys=True)
    else:
        print data
        



results = query_by_name(ARTIST_URL, query_type["simple"], "Queen")
pretty_print(results)

    

    

    
        
        

    


# In[84]:

artist_id = results["artists"][1]["id"]
print "\nARTIST:"
pretty_print(results["artists"][1])


# In[86]:

artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
releases = artist_data["releases"]
print "\nONE RELEASE:"
pretty_print(releases[0], indent=2)
release_titles = [r["title"] for r in releases]


# In[88]:

print "\nALL TITLES:"
for t in release_titles:
     print t


# In[11]:

filename='745090.csv'
import csv
import os

def read_filename(filename):
    data=[]
    with open(filename,'rb') as sd:
        reader =csv.reader(sd)
        for line in reader:
             data.append(line)
        
    
    return data


# In[19]:

d=read_filename(filename)
#pprint.pprint(d)
d



# In[20]:

d[0][1]


# In[26]:

def g(filename):
    data=[]
    with open(filename,'rb') as sd:
        reader=csv.reader(sd)
        robj= reader.next()
        for row in robj:
            data.append(row)
          
    
    return data


# In[28]:

d=g(filename)
d


# In[30]:

d[1]


# In[48]:


# reading a csv file and extracting the name of the source and the header seperately using next()
def dfile(filename):
    data=[]
    with open(filename,'rb') as df:
        r=csv.reader(df)
        name=r.next()[0]
        header=r.next()[0]
        f=r.next()[1]
        data=[row for row in r]
            
    print name
    print header
    print f
    return data


# In[49]:

dfile(filename)


# In[92]:

# problem set1
'''
In this code everytime we call next , the iterator put the pointer at the next line
so , first we called next()[1] to fetch the name from the first row, then we called next() to extract the header,so that
the data does not contain the header and the first row.
'''
import csv
datafile='745090.csv'

def parse_file(datafile):
    data=[]
    with open(datafile, 'rb') as sd:
        r=csv.reader(sd)
        name=r.next()[1]        
        header=r.next()
        data=[row for row in r]
        
    print name
    ##print header
    return data


# In[93]:

data=parse_file(datafile)


# In[94]:

data


# In[122]:

# Using reader instead of DictReader will create list of list
# DictReader creates list of dictionary

datafile='745090.csv'
def parse_file(datafile):
    data=[]
    with open(datafile,'rb') as sd:
        r=csv.reader(sd)          ## r=csv.DictReader(sd)
        data=[row for row in r]
        
    return data


# In[123]:

parse_file(datafile)


# In[140]:

## Working on xl file and writting the contents to a cvs file with | as a delimiter
import xlrd
datafile='2013_ERCOT_Hourly_Load_Data.xls'
outfile = "2013_Max_Loads.csv"
def parse_xlfile(datafile):
    workbook=xlrd.open_workbook(datafile)
    sheet=workbook.sheet_by_index(0)
    data={}
    for n in range(1,9):
        cv=sheet.col_values(n,start_rowx=1,end_rowx=None)
        maxval=max(cv)
        maxpos=cv.index(maxval)+1
        maxtime=sheet.cell_value(maxpos,0)
        realtime=xlrd.xldate_as_tuple(maxtime,0)
        station=sheet.cell_value(0,n)
        data[station]={
            "maxval": maxval,
            "maxtime":realtime
        }
    return data


def save_file(data,outfile):
    with open(outfile,'w') as f:
        w=csv.writer(f,delimiter='|')
        w.writerow(['Station','Year','Month','Day','Hour','Max Load'])
        for s in data:
            year,month,day,hour,_,_=data[s]['maxtime']
            w.writerow([s,year,month,day,hour,data[s]['maxval']])
            
            
            


# In[141]:

data=parse_xlfile(datafile)
save_file(data,outfile)


# In[162]:

import json
import codecs
import requests

URL_MAIN = "http://api.nytimes.com/svc/"
URL_POPULAR = URL_MAIN + "mostpopular/v2/"
API_KEY = { "popular": "35fef37e165b9f9220d6a22918f9e733:12:74839689",
            "article": "8ca1c98c705a547817f71c4d3ea3e887:2:74839689"}


def query_site(url, target, offset):
    # This will set up the query with the API key and offset
    # Web services often use offset paramter to return data in small chunks
    # NYTimes returns 20 articles per request, if you want the next 20
    # You have to provide the offset parameter
    if API_KEY["popular"] == "" or API_KEY["article"] == "":
        print "You need to register for NYTimes Developer account to run this program."
        print "See Intructor notes for information"
        return False
    params = {"api-key": API_KEY[target], "offset": offset}
    r = requests.get(url, params = params)

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()
        
        
        
def get_popular(url, kind, days, section="Technology", offset=0):
    # This function will construct the query according to the requirements of the site
    # and return the data, or print an error message if called incorrectly
    if days not in [1,7,30]:
        print "Time period can be 1,7, 30 days only"
        return False
    if kind not in ["viewed", "shared", "emailed"]:
        print "kind can be only one of viewed/shared/emailed"
        return False

    url += "most{0}/{1}/{2}.json".format(kind, section, days)
    data = query_site(url, "popular", offset)
    print url
    return data


def save_file(kind, period):
    # This will process all results, by calling the API repeatedly with supplied offset value,
    # combine the data and then write all results in a file.
    data = get_popular(URL_POPULAR, "viewed", 1)
    num_results = data["num_results"]
    full_data = []
    with codecs.open("popular-{0}-{1}.json".format(kind, period), encoding='utf-8', mode='w') as v:
        for offset in range(0, num_results, 20):        
            data = get_popular(URL_POPULAR, kind, period, offset=offset)
            full_data += data["results"]
        
        v.write(json.dumps(full_data, indent=2))


# In[163]:

save_file('viewed',1)


# In[165]:

url='http://api.nytimes.com/svc/mostpopular/v2/mostemailed/Technology/1.json?api-key=35fef37e165b9f9220d6a22918f9e733:12:74839689'
            


# In[274]:

import json
import codecs
import requests

URL_MAIN = "http://api.nytimes.com/svc/"
URL_CONGRESS = URL_MAIN + "politics/v3/us/legislative/congress/"
API_KEY = { "popular": "35fef37e165b9f9220d6a22918f9e733:12:74839689",
            "article": "8ca1c98c705a547817f71c4d3ea3e887:2:74839689",
            "congress":"54de5216581a6e83ad9cfcbc1f79885b:2:74839689" }


def query_site(url, target, offset):
    # This will set up the query with the API key and offset
    # Web services often use offset paramter to return data in small chunks
    # NYTimes returns 20 articles per request, if you want the next 20
    # You have to provide the offset parameter
    if API_KEY["popular"] == "" or API_KEY["article"] == "" or API_KEY["congress"] == "":
        print "You need to register for NYTimes Developer account to run this program."
        print "See Intructor notes for information"
        return False
    params = {"api-key": API_KEY[target], "offset": offset}
    r = requests.get(url, params = params)

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()
        
        
        
def get_congress(url, congressnumber, chamber, vote="party", offset=0):
    # This function will construct the query according to the requirements of the site
    # and return the data, or print an error message if called incorrectly
    if congressnumber  in [101,102,103,104,105,106,107,108,109,110,111,112,113]:
        print "Congress number must be valid"
        return False
    if chamber not in ["house", "senate"]:
        print "chamber can be only house or senate"
        return False

    url += "{0}/{1}/votes/{2}.json".format(congressnumber,chamber,vote)
    data = query_site(url, "congress", offset)
    print url
    return data


def save_file(congressnumber,chamber):
    # This will process all results, by calling the API repeatedly with supplied offset value,
    # combine the data and then write all results in a file.
    data = get_congress(URL_CONGRESS, "101", "senate")
    ##data= data['results']
    ##return data
    ##num_results = data{"num_results"}
    full_data = []
    with codecs.open("congress-{0}-{1}.json".format(congressnumber, chamber), encoding='utf-8', mode='w') as v:
        ##for offset in range(0,101, 20):        
            data = get_congress(URL_CONGRESS, congressnumber, chamber, offset=0)
            full_data += data["results"]
        
            v.write(json.dumps(full_data, indent=2))

def get_from_file(congressnumber,chamber):
    filename="congress-{0}-{1}.json".format(congressnumber, chamber)
    with open (filename,'r') as f:
        return json.loads(f.read())


# In[280]:

##data=save_file('101','senate')
##data[[1]]
d=get_from_file('101','senate')
for data in d:
    print data[['name']]


# In[247]:

def article_overview(kind, period):
    data = get_from_file(kind, period)
    titles = []
    urls =[]

    for article in data:
        section = article["section"]
        title = article["title"]
        titles.append({section: title})
        if "media" in article:
            for m in article["media"]:
                for mm in m["media-metadata"]:
                    if mm["format"] == "Standard Thumbnail":
                        urls.append(mm["url"])
    return (titles, urls)


# In[284]:

import xml.etree.ElementTree as ET
article_file='exampleResearchArticle.xml'



# In[296]:

tree=ET.parse(article_file)
root=tree.getroot()
title=root.find('./fm/bibl/title')
for p in title:
    print p.text


# In[299]:

tree=ET.parse(article_file)
root=tree.getroot()
a=root.findall('./fm/bibl/aug/au')
for el in a:
    email=el.find('email')
    print email.text
    


# In[304]:

tree=ET.parse(article_file)
root=tree.getroot()
al=root.findall('./fm/bibl/aug/au')
author=[]
for a in al:
    snm=a.find('snm')
    fnm=a.find('fnm')
    email=a.find('email')
    print snm.text,fnm.text,email.text
    data={
        'snm':snm.text,
        'fnm':fnm.text,
        'email':email.text
    }
    author.append(data)


# In[305]:

author


# In[308]:

tree=ET.parse(article_file)
root=tree.getroot()
ref=root.find('./fm/bibl/xrefbib/pubidlist')


# In[311]:

pubid=ref.findall('pubid')
for p in pubid:
    print p.text


# In[313]:

def get_author(article_file):
    tree=ET.parse(article_file)
    root=tree.getroot()
    author=[]
    for a in root.findall('./fm/bibl/aug/au'):
        data={
            'snm':None,
            'fnm':None,
            'email':None
            
        }
        data['snm']=a.find('snm').text
        data['fnm']=a.find('fnm').text
        data['email']=a.find('email').text
        author.append(data)
    return author   


# In[316]:

get_author(article_file)


# In[327]:

tree=ET.parse(article_file)
root=tree.getroot()
al=root.findall('./fm/bibl/aug/au')
author=[]
for a in al:
    data={
        "snm":None,
        "fnm":None,
        "email":None,
        "insr":[]
    }
    data["snm"]=a.find('snm').text
    data["fnm"]=a.find('fnm').text
    data["email"]=a.find('email').text
    insr=a.findall('insr')
    for i in insr:
        data['insr'].append(i.attrib['iid'])
    author.append(data)


# In[328]:

author


# In[329]:

tree=ET.parse(article_file)
root=tree.getroot()
au=root.findall('./fm/bibl/aug/au')


# In[335]:

# Checking out the attribute of the tags
for i in au:
    snm=i.find('snm').text
    fnm=i.find('fnm').text
    email=i.find('email').text
    print snm
    print fnm
    print email
    
    insr=[]
    ins=i.findall('insr')
    for ins in ins:
        insr.append(ins.attrib['iid'])
    print insr


# In[336]:




# In[345]:

from bs4 import BeautifulSoup
import requests

html_page='page_source.html'


# scrape the html page to extract the value of a form data eventvalidation & viewsstate and storing it in the dictionary

def extract_data(html_page):
    data={
          'eventvalidation':None,
          'viewstate':None
         }
    with open(html_page,'r') as html:
        soup=BeautifulSoup(html,'lxml')
        ev=soup.find(id="__EVENTVALIDATION")
        data['eventvalidation']=ev['value']
    
        vs=soup.find(id="__VIEWSTATE")
        data['viewstate']=vs['value']
    return data


# In[378]:

data=extract_data(html_page)
eventvalidation=data['eventvalidation']
viewstate=data['viewstate']


# In[394]:

## Scrapping the html page to extract all the options in the carrier dropdown and store it in a 
def extract_carrieroptions(html_page):
    carr=[]
    with open(html_page,'r') as html:
        soup=BeautifulSoup(html,'lxml')
        carrier=soup.find(id="CarrierList")
        options=carrier.find_all('option')
        for options in options:
            if options['value'] =='All' or options['value'] =='AllUS' or options['value'] =='AllForeign':
                pass
            else:
                carr.append(options['value'])
    
    
    return carr
            
    
    


# In[395]:

carriers=extract_carrieroptions(html_page)
carriers


# In[366]:

## scrape the web to extract all the options for airport drop down and store it in a list
def extract_airportlist(html_page):
    airports=[]
    with open(html_page,'r') as html:
        soup=BeautifulSoup(html,"lxml")
        air=soup.find(id="AirportList")
        options=air.find_all('option')
        for options in options:
            airports.append(options['value'])
            
    return airports
        


# In[391]:

carriers


# In[397]:

airports=(extract_airportlist(html_page))
airports


# In[385]:

# make the post httprequest and send it
r=requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
               data={'AirportList':airports[4],
                     'CarrierList':carriers[16],
                     'Submit':'Submit',
                     '__EVENTTARGET':"",
                     '__EVENTARGUMENT':"",
                     '__EVENTVALIDATION':eventvalidation,
                     '__VIEWSTATE':viewstate
                           
    })


# In[384]:

f=open('virgin_and_logan_airport.html','w')
f.write(r.text)


# In[405]:

from bs4 import BeautifulSoup

s=requests.Session()

r=s.get("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2")
soup=BeautifulSoup(r.text)
vs=soup.find(id="__VIEWSTATE")
viewstate=vs['value']
ev=soup.find(id="__EVENTVALIDATION")
eventvalidation=ev['value']

r=s.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
               data={'AirportList':'BOS',
                     'CarrierList':'VX',
                     'Submit':'Submit',
                     '__EVENTTARGET':"",
                     '__EVENTARGUMENT':"",
                     '__EVENTVALIDATION':eventvalidation,
                     '__VIEWSTATE':viewstate
                           
    })

f=open('virgin_and_logan_airport2.html','w')
f.write(r.text)


# In[406]:

#Problem set1 for screen scrapping - lesson 2 Data in more complex formats

html_page='options.html'

def extract_carrieroptions(html_page):
    carr=[]
    with open(html_page,'r') as html:
        soup=BeautifulSoup(html,'lxml')
        carrier=soup.find(id="CarrierList")
        options=carrier.find_all('option')
        for options in options:
            if options['value'] =='All' or options['value'] =='AllUS' or options['value'] =='AllForeign':
                pass
            else:
                carr.append(options['value'])
    
    
    return carr

carriers=extract_carrieroptions(html_page)
carriers
    


# In[407]:

html_page='options.html'
def extract_airportlist(html_page):
    airports=[]
    with open(html_page,'r') as html:
        soup=BeautifulSoup(html,"lxml")
        air=soup.find(id="AirportList")
        options=air.find_all('option')
        for options in options:
            if options['value'] =='All' or options['value'] =='AllMajors' or options['value'] =='AllOthers':
                pass
            else:
                airports.append(options['value'])
            
    return airports


airports=(extract_airportlist(html_page))
airports


# In[402]:

from bs4 import BeautifulSoup

s=requests.Session()

r=s.get("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2")
soup=BeautifulSoup(r.text)
vs=soup.find(id="__VIEWSTATE")
viewstate=vs['value']
ev=soup.find(id="__EVENTVALIDATION")
eventvalidation=ev['value']
carrier='FL'
airport='ATL'
r=s.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
               data={'AirportList':airport,
                     'CarrierList':carrier,
                     'Submit':'Submit',
                     '__EVENTTARGET':"",
                     '__EVENTARGUMENT':"",
                     '__EVENTVALIDATION':eventvalidation,
                     '__VIEWSTATE':viewstate
                           
    })

f=open('data/{}-{}.html'.format(carrier,airport),'w')
f.write(r.text)


# In[408]:

#Problem set1 for screen scrapping - lesson 2 Data in more complex formats

html_page='virgin_and_logan_airport1.html'

def extract_carrieroptions(html_page):
    carr=[]
    with open(html_page,'r') as html:
        soup=BeautifulSoup(html,'lxml')
        carrier=soup.find(id="CarrierList")
        options=carrier.find_all('option')
        for options in options:
            if options['value'] =='All' or options['value'] =='AllUS' or options['value'] =='AllForeign':
                pass
            else:
                carr.append(options['value'])
    
    
    return carr

carriers=extract_carrieroptions(html_page)
carriers
    


# In[409]:

html_page='virgin_and_logan_airport1.html'
def extract_airportlist(html_page):
    airports=[]
    with open(html_page,'r') as html:
        soup=BeautifulSoup(html,"lxml")
        air=soup.find(id="AirportList")
        options=air.find_all('option')
        for options in options:
            if options['value'] =='All' or options['value'] =='AllMajors' or options['value'] =='AllOthers':
                pass
            else:
                airports.append(options['value'])
            
    return airports


airports=(extract_airportlist(html_page))
airports


# In[458]:

page='data/FL-ATL.html'
from bs4 import BeautifulSoup

with open(page,'r') as html:
    soup=BeautifulSoup(html)
    a=soup.find("table", {"class":"dataTDRight"})
    summary=soup.find_all("tr", {"class":"dataTDRight"})
    


# In[478]:

summary


# In[470]:

summary[0].findAll("td")


# In[532]:

page='options.html'
from bs4 import BeautifulSoup

with open(page,'r') as html:
    soup=BeautifulSoup(html)
    a=soup.find("table", {"class":"dataTDRight"})
    summary=soup.find_all("tr", {"class":"dataTDRight"})

data=[]

for i in range(len(summary)):
    rows=summary[i].findAll("td")
    for td in rows:
        text=td.find(text=True)
        if text =="TOTAL":
            pass
        else:
            data.append(text)
        


# In[533]:

data


# In[ ]:




# In[519]:

from pandas import Series,DataFrame
data1=Series(data)


# In[523]:

data1


# In[530]:

year=[]
for i in range(len(data1)):
    if i in [0,5,10,15]:
        year.append(data1[i])
    
year


# In[517]:

'''
page='data/FL-ATL.html'
from bs4 import BeautifulSoup

with open(page,'r') as html:
    soup=BeautifulSoup(html)
    a=soup.find("table", {"class":"dataTDRight"})
    summary=soup.find_all("tr", {"class":"dataTDRight"})
    
'''

data1=[{"courier": None,
             "airport": None,
             "year": None,
             "month": None,
             "flights": {"domestic": None,
                         "international": None}
            },
      {"courier": None,
             "airport": None,
             "year": None,
             "month": None,
             "flights": {"domestic": None,
                         "international": None}
            },
       {"courier": None,
             "airport": None,
             "year": None,
             "month": None,
             "flights": {"domestic": None,
                         "international": None}
            },
       {"courier": None,
             "airport": None,
             "year": None,
             "month": None,
             "flights": {"domestic": None,
                         "international": None}
            }
     ]

for i in range(len(summary)):
    rows=summary[i].findAll("td")
    for td in rows:
        text=td.find(text=True)
        if text =="TOTAL":
            pass
        else:
            data1[i]['courier']="FL"
            data1[i]['airport']="ATL"
            
    for td in rows:
        text=td.find(text=True)
        print "text"+str(i), text
        


# In[509]:

data1


# In[494]:

d=[{
    "courier": "FL",
             "airport": "ATL",
             "year": 2002,
             "month": 10,
             "flights": {"domestic": 100,
                         "international": 1000}
},
   {
        "courier": "FL",
             "airport": "ATL",
             "year": 2002,
             "month": 12,
             "flights": {"domestic": 200,
                         "international": 1800}
    }
   ]


# In[502]:

data


# In[553]:

data=[]
info={}

page="data/FL-ATL.html"
with open (page,'r') as html:
    soup=BeautifulSoup(html,'lxml')
    trid=soup.find(id='DataGrid1')
    tr=trid.find_all("tr",{"class":"dataTDRight"})
    ## the dataTDRight can also be found by tr=soup.find_all("tr", {"class":"dataTDRight"})
    for t in tr:
        td=t.find_all("td")
        if td[1].text!="TOTAL":
            info['year']=int(td[0].text)
            info['month']=int(td[1].text)
            flight_details={}
            flight_details['domestic']=int(td[2].text.replace(',',''))
            flight_details['international']=int(td[3].text.replace(',',''))
            info['flights']=flight_details
          
            data.append(info)
        


# In[554]:

data


# In[579]:

data=[]
results=[]
filename="PatentData.xml"
n=0
with open(filename,'rb') as f:
    flines=f.readlines()
    for i in range(len(flines)):
        line=flines[i]
        if line.startswith("<?xml") and len(data) > 0:
                results.append(data)
                data=[]
        else:
            data.append(line)
            
        if (i==len(flines)-1):
            results.append(data)

for res in results:
    tre=ET.ElementTree(ET.fromstringlist(res))
    new_file="{}-{}".format(filename,n)
    n+=1
    tre.write(new_file,xml_declaration=True,method="xml",encoding="UTF-8")


# In[568]:

results


# In[ ]:



