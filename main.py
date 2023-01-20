# Dark-Hydro by: Euronymou5
# https://github.com/Euronymou5
# https://twitter.com/Euronymou51

import os
import opencage
from opencage.geocoder import OpenCageGeocode
import phonenumbers
import json
from phonenumbers import geocoder
import requests
from googlesearch import search
import random
import time
from colorama import Fore

logo = f"""{Fore.MAGENTA}
██████   █████  ██████  ██   ██       ██   ██ ██    ██ ██████  ██████   ██████  
██   ██ ██   ██ ██   ██ ██  ██        ██   ██  ██  ██  ██   ██ ██   ██ ██    ██ 
██   ██ ███████ ██████  █████   █████ ███████   ████   ██   ██ ██████  ██    ██ 
██   ██ ██   ██ ██   ██ ██  ██        ██   ██    ██    ██   ██ ██   ██ ██    ██ 
██████  ██   ██ ██   ██ ██   ██       ██   ██    ██    ██████  ██   ██  ██████ 
"""

with open('config.json', 'r') as configuracion:
  configuracion_dat = json.load(configuracion)

def clear():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

  
def menu():
  clear()
  print(logo)
  dom = ["com","com.tw","co.in","be","de","co.uk","co.ma","dz","ru","ca"]
  numero = input(f'{Fore.BLUE}[~] Ingresa un numero telefonico: ')
  time.sleep(2)
  # ---- NumVerify ----- #
  api = f"https://api.apilayer.com/number_verification/validate?number={numero}"
  try:
    key = configuracion_dat['Numverifykey']
    apikey = {
      "apikey": key,
    }
    payload = {}
    lol = requests.request("GET", api, headers=apikey, data = payload).json()
    if lol['valid'] == False:
       print(f'{Fore.RED}\n[!] El numero no es valido!')
       exit()
    else:
      print('\n[~] Numero: ', lol['number'])
      print('[~] Codigo del pais: ', lol['country_code'])
      print('[~] Nombre del pais: ', lol['country_name'])
      print('[~] Ubicacion: ', lol['location'])
      print('[~] Transportador: ', lol['carrier'])
  except KeyError:
     print(f'{Fore.RED}\n[!] A ocurrido un error.')
  # --- Opencage --- #
  geo = OpenCageGeocode(configuracion_dat['OpencageKey'])
  phone = phonenumbers.parse(numero)
  location = geocoder.description_for_number(phone, 'en')
  query = str(location)
  results = geo.geocode(query)
  lat = results[0]['geometry']['lat']
  lng = results[0]['geometry']['lng']
  # --- Phonenumbers --- #
  print(f'\n[~] Pais: {location}')
  print(f'[~] Latitud: {lat}')
  print(f'[~] Longitud: {lng}')
  # --- Dorking --- #
  print('\n[~] Realizando busqueda con dorking...')
  time.sleep(2)
  tld = random.choice(dom)
  command = f'intext:{numero}'
  command2 = f"site:@ filetype:PDF intext:{numero}"
  command3 = f"site:facebook.com intext:{numero}"
  command4 = f"site:twitter.com intext:{numero}"
  command5 = f"site:instagram.com intext:{numero}"
  for j in search(command, tld, num=10, stop=10, pause=2):
    print(f'{Fore.GREEN}\nResultados encontrados!: {j}')
  print('\n[~] Buscando numero telefonico en archivos pdf...')
  for i in search(command2, tld, num=10, stop=10, pause=2):
    print(f'\nResultados encontrados!: {i}')
  print('\n[~] Buscando numero telefonico en redes sociales..')
  for a in search(command3, tld, num=10, stop=10, pause=2):
    print(f'\nResultados encontrados!: {a}')
  for b in search(command4, tld, num=10, stop=10, pause=2):
    print(f'\nResultados encontrados!: {b}')
  for c in search(command5, tld, num=10, stop=10, pause=2):
    print(f'\nResultados encontrados!: {c}')


menu()
