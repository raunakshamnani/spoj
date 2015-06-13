from bs4 import BeautifulSoup
import requests
import csv
from array import *


movie_name = []
movie_director = []
movie_cast = []
movie_genre = []
# movie_music = []

link = "http://en.wikipedia.org/wiki/List_of_Bollywood_films_of_2015"
r  = requests.get(link)
data = r.text
soup = BeautifulSoup(data)


for table in soup.find_all('table' , class_="wikitable"):
	flag = 0
	flag1 = 0
	# if (flag1 == 0):
	# 	flag1 = flag1 + 1
	# 	continue

	for row in table.find_all('tr'):
		if (flag == 0 or flag == 1):
			flag = flag + 1
			continue

		data = row.find_all('td')
		print (len(data))
		print (data[-3].text.encode('cp850', errors='replace').decode('cp850'))
		if (data[0].text == "Insaaf"):
			continue
		if (data[0].text == "Chota Jadugar"):
			continue
		if (data[0].text == "Jeeo Shaan Se"):
			continue
		if (data[0].text == "Jodidar"):
			continue
		if (data[0].text == "Dhaai Akshar Prem Ke"):
			continue
		if (data[-3].text == "Tere Bin Laden"):
			continue

		movie_name.append (data[-5].text)
		movie_director.append (data[-3].text)
		movie_cast.append (data[-2].text)
		movie_genre.append (data[-4].text)
		# movie_music.append (data[4].text)

final = zip(movie_name , movie_director , movie_cast , movie_genre)

with open('wiki_movie_2015.csv' , 'w') as c:
	writer = csv.writer(c , lineterminator='\n')
	writer.writerow(['Name' , 'Director'  , 'Cast' , 'Genre'])
	for route in final:
		writer.writerow([route[0] , route[1] , route[2] , route[3]])
c.close()



