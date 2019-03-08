import pandas as pd


import urllib.request, json 

#Getting the data from  the given link 
with urllib.request.urlopen("https://itunes.apple.com/us/rss/topalbums/limit=100/json") as url:
#using json loads conevrting to a string object to json type
    data = json.loads(url.read().decode())
#Parsing the feed and entry object gives the list of 100 objects
    entity=data['feed']['entry']
    print(entity)
    for obj in entity:
	    print(obj)