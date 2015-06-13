from bs4 import BeautifulSoup
import requests
import csv
from array import *

name = []
father = []
dob = []
year_of_info = []
registration = []
date = []
state = []
qualification = []
qualification_year = []
university = []
address = []

for i in range (60001 , 70001):
	j = str(i);
	link = "http://www.mciindia.org/ViewDetails.aspx?ID="
	link = link + j
	print (link)
	one_doctor = []
	r  = requests.get(link)
	data = r.text
	soup = BeautifulSoup(data)
	count = 0

	for doc_name in soup.find_all('span' , class_="label"):
		# print (doc_name.text)

		if (count == 0):
			name.append(doc_name.text)
		elif (count == 1):
			father.append(doc_name.text)
		elif (count == 2):
			dob.append(doc_name.text)
		elif (count == 3):
			year_of_info.append(doc_name.text)
		elif (count == 4):
			registration.append(doc_name.text)
		elif (count == 5):
			date.append(doc_name.text)
		elif (count == 6):
			state.append(doc_name.text)
		elif (count == 7):
			qualification.append(doc_name.text)
		elif (count == 8):
			qualification_year.append(doc_name.text)
		elif (count == 9):
			university.append(doc_name.text)
		elif (count == 10):
			address.append(doc_name.text)

		count = count + 1
final= zip (name , father , dob , year_of_info , registration , date , state , qualification , qualification_year , university , address)

with open('doctor.csv', 'w') as c:
	writer = csv.writer(c , lineterminator='\n')
	writer.writerow(['Name' , 'Father Name' , 'DOB' , 'Year Of Info' , 'Registration Number' , 'Date' , 'State' , 'qualification' , 'qualification_year' , 'university' , 'address'])
	for route in final:
		writer.writerow([route[0] , route[1] , route[2] , route[3] , route[4] , route[5] , route[6] , route[7] , route[8] , route[9] , route[10]])
c.close()
