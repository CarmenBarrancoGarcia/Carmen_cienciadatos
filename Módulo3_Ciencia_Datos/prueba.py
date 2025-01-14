import requests
import bs4 # Para ver la versión
from bs4 import BeautifulSoup
from time import sleep

response = requests.get('https://www.recetasgratis.net/Recetas-de-Ensaladas-listado_receta-4_1.html')
soup = BeautifulSoup(response.text, "html.parser")
soup.body