from bs4 import BeautifulSoup
import requests
import csv
from array import *

name = []
address = []

for i in range(1,6):
	link = "https://retailmaharashtra.wordpress.com/2009/03/20/medical-stores-in-mumbai-list-"
	link = link + str(i)
	r  = requests.get(link)
	data = r.text
	soup = BeautifulSoup(data)

	for store in soup.find_all('td'):
		add_tags = store.find_all('b')
		for add_tag in add_tags:
			print ("Name : " + add_tag.text)
			name.append(add_tag.text)
			add_tag.extract()
		print ("Address : " + store.text)
		address.append(store.text)
final = zip (name , address)

with open('medical_retailmaharashtra.csv', 'w') as c:
	writer = csv.writer(c , lineterminator='\n')
	writer.writerow(['Name' , 'Address'])
	for route in final:
		writer.writerow([route[0] , route[1]])
c.close()
