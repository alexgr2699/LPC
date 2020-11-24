import tkinter
import requests
from bs4 import BeautifulSoup
import re

def buscador(palabra):
	url = "https://revistabyte.es/ciberseguridad/"
	response = requests.get(url)
	html = BeautifulSoup(response.content, 'html.parser')
	a = html.find_all('a')
	i=0
	for x in a:
		t = x.text.strip()
		m = re.search(palabra, t)
		if str(m) != "None":
			i=i+1
			print("PAGINA ",i)
			url2 = x.get('href')
			response2 = requests.get(url2)
			html2 = BeautifulSoup(response2.content, 'html.parser')
			p = html2.find_all('p')
			for x2 in p:
				t2 = x2.text.strip()
				print(t2)
				break

def PB():
	palabra = cajaTexto.get()
	return palabra		

ventana = tkinter.Tk()
ventana.geometry("225x125")

instruccion = tkinter.Label(ventana, text = "¿Cual es la palabra que quiere buscar?\n(malware, ciberseguridad, etc..) ")
instruccion.pack()

cajaTexto = tkinter.Entry(ventana)
cajaTexto.pack()

boton = tkinter.Button(ventana, text = "Buscar", padx = 20, pady =10, command = lambda: buscador(PB()))
boton.pack()

ventana.mainloop()