from bs4 import BeautifulSoup
import requests
import csv
from array import *


shop_name = []
shop_city = []
shop_state = []

for i in range ( 97 , 123 ):

	link = "http://www.medindia.net/buy_n_sell/chemist/chemist_result.asp?alpha="+chr(i)
	r  = requests.get(link)
	data = r.text
	soup = BeautifulSoup(data)

	p1 = soup.find_all('p' , class_="searchtext")

	p2 = p1[1].find_all('b')
	length = int(p2[2].text)

	for j in range( 1 , length ):

		link = "http://www.medindia.net/buy_n_sell/chemist/chemist_result.asp?alpha="+chr(i)+"&page="+str(j)

		r  = requests.get(link)
		data = r.text
		soup = BeautifulSoup(data)

		print (link)

		for store in soup.find_all('div' , class_="article-content"):

			for name in store.find_all('a'):
				print ("\nName : " + name.text)
				shop_name.append(name.text)
				name.extract()

			for state in store.find_all('p' , class_="speciality"):
				print ("State : " + state.text)
				shop_state.append(state.text)
				state.extract()

			for city in store.find_all('span'):
				print ("City : " + (city.text)[2:])
				shop_city.append(city.text[2:])
				city.extract()

final = zip (shop_name , shop_city , shop_state)

with open('medindia.csv' , 'w') as c:
	writer = csv.writer(c , lineterminator='\n')
	writer.writerow(['Name' , 'City' , 'State'])
	for route in final:
		writer.writerow([route[0] , route[1] , route[2]])
c.close()





