import requests
import pymongo


client = pymongo.MongoClient("mongodb+srv://admin:lLBoZmX3ZMR3JVv7@cluster0.jknnc.mongodb.net/?retryWrites=true&w=majority")
db = client["website"]
collection = db["data"]
import string
import random
dummy=''
print('Hi')
print(collection)
N = 10
f=0
while True:
	while collection.count_documents({'wrong':dummy})==1 or f==0:
		dummy=''.join(random.choices(string.ascii_lowercase+string.digits, k=N))
	print(dummy,'dummy')
	url='https://byte-by-byte.wistia.com/medias/'+dummy
	print(url)
	x = requests.get(url)
	print(len(x.links))
	if len(x.links)>=1:
		collection.insert_one({'url':url})
		print(collection.find())
	else:
		collection.insert_one({'wrong':dummy})
	f=1
