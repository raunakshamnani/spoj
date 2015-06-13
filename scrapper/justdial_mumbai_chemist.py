from bs4 import BeautifulSoup
import requests
import csv
from array import *


shop_name = []
shop_number = []
shop_address = []
shop_rating = []
shop_year = []
shop_x_coordinate = []
shop_y_coordinate = []
shop_monday = []
shop_tuesday = []
shop_wednesday = []
shop_thursday = []
shop_friday = []
shop_saturday = []
shop_sunday = []


# for i in range ( 1 , 21 ) :
for i in range ( 1 , 2 ) :
	link = "http://www.justdial.com/Mumbai/24-Hours-Chemists/ct-4406/page-" + str(i)
	r  = requests.get(link)
	data = r.text
	soup = BeautifulSoup(data)


	for medical in soup.find_all('span' , class_="jcn"):

		print ("Length \n")

		print ("Shop Name : " + str(len(shop_name)))
		if (len(shop_number) != len(shop_name)):
			shop_number.append("")
		print ("Shop Number : " + str(len(shop_number)))

		if (len(shop_name) != len(shop_address)):
			shop_address.append("")
		print ("Shop Address : " + str(len(shop_address)))

		if (len(shop_name) != len(shop_rating)):
			shop_rating.append("")
		print ("Shop Rating : " + str(len(shop_rating)))

		if (len(shop_name) != len(shop_year)):
			shop_year.append("")
		print ("Shop Year : " + str(len(shop_year)))

		if (len(shop_name) != len(shop_x_coordinate)):
			shop_x_coordinate.append("")
		print ("Shop X : " + str(len(shop_x_coordinate)))

		if (len(shop_name) != len(shop_y_coordinate)):
			shop_y_coordinate.append("")
		print ("Shop Y : " + str(len(shop_y_coordinate)))

		if (len(shop_name) != len(shop_sunday)):
			shop_sunday.append("")
		print ("Shop Sunday : " + str(len(shop_sunday)))

		if (len(shop_name) != len(shop_monday)):
			shop_monday.append("")
		print ("Shop Monday : " + str(len(shop_monday)))

		if (len(shop_name) != len(shop_tuesday)):
			shop_tuesday.append("")
		print ("Shop Tuesday : " + str(len(shop_tuesday)))

		if (len(shop_name) != len(shop_wednesday)):
			shop_wednesday.append("")
		print ("Shop Wednesday : " + str(len(shop_wednesday)))

		if (len(shop_number) != len(shop_thursday)):
			shop_thursday.append("")
		print ("Shop Thursday : " + str(len(shop_thursday)))

		if (len(shop_number) != len(shop_friday)):
			shop_friday.append("")
		print ("Shop Friday : " + str(len(shop_friday)))

		if (len(shop_number) != len(shop_saturday)):
			shop_saturday.append("")
		print ("Shop Saturday : " + str(len(shop_saturday)))

		for new_link in medical.find_all('a'):
			r2  = requests.get(new_link['href'])
			data2 = r2.text
			soup2 = BeautifulSoup(data2)

			'''Name'''
			for name in soup2.find_all('span' , class_="fn"):
				print ("\n\n\nName : " + name.text[8:])
				shop_name.append (name.text[8:])


			'''Number'''
			for continfo in soup2.find_all('aside' , class_="continfo"):
				# print ("Info : " + continfo.text)
				for number in continfo.find_all('a' , class_="tel"):
					print ("Number : " + number.text[6:])
					shop_number.append (number.text[6:])
					break
	
				for view_map in continfo.find_all('a'):
					view_map.extract()
				
				'''Address'''
				for address in continfo.find_all('span' , class_="jaddt"):
					print ("Address : " + address.text[8:-15])
					shop_address.append (address.text[8:-15])
					final_address = address.text[8:-15]
					


			'''Year OF Establishment'''
			for year in soup2.find_all('span' , class_="rtngna"):
				print ("Year : " + year.text)
				shop_year.append (year.text)


			'''Votes'''
			for votes in soup2.find_all('span' , class_="votes"):
				print ("Rating : " + votes.text[18:])
				shop_rating.append (votes.text[18:])


			for maps in soup2.find_all('a' , class_="mapicn"):
				map_link = "http://wap.justdial.com/search.php?&docid=" + (maps['onclick'])[10:-40] + "&stype=detail&city=Mumbai&m=1"
				r3  = requests.get(map_link)
				data3 = r3.text
				soup3 = BeautifulSoup(data3)

				''' Coordinates'''
				flag = 0
				for mapes in soup3.find_all('div' , class_="tabcont"):
					for maps in mapes.find_all('a' , class_="la"):
						map_coordinate_text = maps['onclick']
						if (flag == 0):
							print ("X : " + map_coordinate_text[40:55])
							print ("Y : " + map_coordinate_text[58:73])
							shop_x_coordinate.append(map_coordinate_text[40:55])
							shop_y_coordinate.append(map_coordinate_text[58:73])
							flag = 1

				'''Per day Timing'''
				count = 0
				table = soup3.find_all('table')
				for rows in table[1].find_all('tr'):
					table_data = rows.find_all('td')
					print ("Day : " + table_data[0].text)
					print ("Time : " + table_data[2].text)
					count = count + 1
					if (count == 1):
						shop_monday.append(table_data[2].text)
					elif (count == 2):
						shop_tuesday.append(table_data[2].text)
					elif (count == 3):
						shop_wednesday.append(table_data[2].text)
					elif (count == 4):
						shop_thursday.append(table_data[2].text)
					elif (count == 5):
						shop_friday.append(table_data[2].text)
					elif (count == 6):
						shop_saturday.append(table_data[2].text)
					elif (count == 7):
						shop_sunday.append(table_data[2].text)



final = zip (shop_name,shop_number,shop_address,shop_rating,shop_year,shop_x_coordinate,shop_y_coordinate,shop_monday,shop_tuesday,shop_wednesday,shop_thursday,shop_friday,shop_saturday,shop_sunday)

with open('justdial.csv' , 'w') as c:
	writer = csv.writer(c , lineterminator='\n')
	writer.writerow(['Name','Number','Address','Rating','Year','X','Y','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
	for route in final:
		writer.writerow([route[0],route[1],route[2],route[3],route[4],route[5],route[6],route[7],route[8],route[9],route[10],route[11],route[12],route[13]])
c.close()
