import pandas as pd


import urllib.request, json 

all_data_list=[]
#Getting the data from  the given link 
with urllib.request.urlopen("https://itunes.apple.com/us/rss/topalbums/limit=100/json") as url:
#using json loads conevrting to a string object to json type
    data = json.loads(url.read().decode())
#Parsing the feed and entry object gives the list of 100 objects where we have the needed data like ID,price,Date etc
    entity=data['feed']['entry']
	
    for obj in entity:
        append_list=[]
        ID=obj['id']['attributes']['im:id']
        append_list.append(ID)
        category=obj['category']['attributes']['label']
        append_list.append(category)
        Name=obj['im:name']['label']
        append_list.append(Name)
        artist=obj['im:artist']['label']
        append_list.append(artist)
        link=obj['link']['attributes']['href']
        append_list.append(link)
        price=obj['im:price']['label']
        append_list.append(price)
        releaseDate=obj['im:releaseDate']['label']
        append_list.append(releaseDate)
        #print(append_list)
		#adding all the needed information into a dataframe
        all_data_list.append(append_list)
#print(all_data_list)

#create empty datafrmae using pandas
df = pd.DataFrame(all_data_list,columns=['ID', 'category', 'Name', 'artist', 'link', 'price','releaseDate'])
df.to_csv("output.csv")


#importing to ftp server
#Trasfer the csv file to a FTP server (Here's FTP conection info - server: test.rebex.net, username: demo, password: password)
from ftplib import FTP  
ftp = FTP('test.rebex.net')  
ftp.login('demo', 'password')  
with open(r"C:\Users\Dilip\Documents\GitHub\Python-Scritpting-Challenge-working-code\Expert\output.csv", 'r') as f:  
    ftp.storlines('STOR %s' % 'output.csv', f)
ftp.quit()



