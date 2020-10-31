import requests
import os
from bs4 import BeautifulSoup

def peliculas()-> BeautifulSoup:
	html = "https://en.wikipedia.org/wiki/List_of_highest-grossing_films"
	response = requests.get(html)
	html = BeautifulSoup(response.content, 'html.parser')	
	tr = html.table.find_all('tr')
	file = open("/Users/alexg/Desktop/peliculas.txt", "w")
	for i in tr:
		etiquetas = i.find_all('i')
		etiquetas += i.find_all('td')
		t = [x.text.strip() for x in etiquetas]
		print(t)
		file.write(str(t) + os.linesep)	

peliculas()