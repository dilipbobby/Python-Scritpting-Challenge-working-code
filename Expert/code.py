import pandas as pd


import urllib.request, json 

#Getting the data from  the given link 
with urllib.request.urlopen("https://itunes.apple.com/us/rss/topalbums/limit=100/json") as url:
#using json loads conevrting to a string object to json type
    data = json.loads(url.read().decode())
#Parsing the feed and entry object gives the list of 100 objects where we have the needed data like ID,price,Date etc
    entity=data['feed']['entry']
    for obj in entity:
        print("ID",obj['id']['attributes']['im:id'])
        print("category",obj['category']['attributes']['label'])
        print("Name",obj['im:name']['label'])
        print("artist",obj['im:artist']['label'])
        print("link",obj['link']['attributes']['href'])
        print("price",obj['im:price']['label'])
        print("date",obj['im:releaseDate']['label'])