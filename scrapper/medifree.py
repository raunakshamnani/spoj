from bs4 import BeautifulSoup
import requests
import csv
from array import *

test_name = []
test_cost = []

center = []
center_address = []
center_number = []

main_link = "http://www.medifee.com"
link = "http://www.medifee.com/dc-in-kolkata"
r  = requests.get(link)
data = r.text
soup = BeautifulSoup(data)
count = 0

for diagnostic in soup.find_all('td'):
	first_line = 1
	if (count == 0):
		for name in diagnostic.find_all('a'):
			'''
			Remove Span tag text from attribute a 
			'''
			spantags = name.find_all('span')
			for spantag in spantags:
				spantag.extract()
			print ("Name : " + name.text)
			
			'''
			Extracting out the Details in More Detail
			'''
			new_link = main_link + name['href']
			print ("Href : " + new_link)

			r2 = requests.get(new_link)
			data2 = r2.text
			soup = BeautifulSoup(data2)
			for rows in soup.find_all('tr'):
				td_list = rows.find_all('td')

				if(first_line):
					first_line = 0
				else:
					test_name.append(td_list[0].text)
					test_cost.append(td_list[1].text)


			test_center = zip (test_name , test_cost)

			center_name = "MEDIFREE/" + name.text + ".csv"
			print (center_name)
			with open(center_name, 'w') as c:
				writer = csv.writer(c , lineterminator='\n')
				writer.writerow(['Test Name' , 'Cost'])
				writer.writerows(test_center)
			c.close()
			center_name = ""

			center.append(name.text)
			name.extract()
		print ("Address : " + diagnostic.text)
		center_address.append(diagnostic.text)
		count = 1
	else:
		print ("Number : " + diagnostic.text + "\n" + "\n")
		center_number.append(diagnostic.text)
		count = 0

final= zip (center , center_address , center_number)
with open('diagnostic.csv', 'w') as c:
	writer = csv.writer(c , lineterminator='\n')
	writer.writerow(['Name' , 'Address' , 'Number'])
	for route in final:
		# print (route[0] , route[1] , route[2])
		writer.writerow([route[0] , route[1] , route[2]])
c.close()
