# Dark-Hydro by: Euronymou5
# https://github.com/Euronymou5
# https://twitter.com/Euronymou51

import requests
import argparse
from colorama import Fore
from opencage.geocoder import OpenCageGeocode
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import os
from googlesearch import search
import subprocess
import json
import random
import time
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-phoneinfoga", action="store_true", help="Añadir escaneo de la tool phoneinfoga.")
parser.add_argument("-numero", "-n", type=str, help="Agregar numero telefonico.")
parser.add_argument("-phonenumbers", action="store_true", help="Añadir escaneo de la libreria phonenumbers.")
parser.add_argument("-numverify", action="store_true", help="Agregar escaneo de numverify.")
parser.add_argument("-opencage", action="store_true", help="Agregar escaneo con opencage.")
parser.add_argument("-abstract", action="store_true", help="Agregar escaneo con abstract api.")
parser.add_argument("-veriphone", action="store_true", help="Agregar escaneo con VeriPhone.")
parser.add_argument("-dork", type=int, help="Agregar escaneo con google dorks.")
args = parser.parse_args()

logo = f"""{Fore.MAGENTA}
██████   █████  ██████  ██   ██       ██   ██ ██    ██ ██████  ██████   ██████  
██   ██ ██   ██ ██   ██ ██  ██        ██   ██  ██  ██  ██   ██ ██   ██ ██    ██ 
██   ██ ███████ ██████  █████   █████ ███████   ████   ██   ██ ██████  ██    ██ 
██   ██ ██   ██ ██   ██ ██  ██        ██   ██    ██    ██   ██ ██   ██ ██    ██ 
██████  ██   ██ ██   ██ ██   ██       ██   ██    ██    ██████  ██   ██  ██████ 

                            {Fore.LIGHTRED_EX} |By: Euronymou5|
""" 

with open('config.json', 'r') as configuracion:
  configuracion_dat = json.load(configuracion)

def clear():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

def scan():
    clear()
    print(logo)
    numero = args.numero
    
    # ---Numverify
    if args.numverify:
       print(f'{Fore.BLUE}\n[~] Realizando escaneo con numverify...')
       time.sleep(2)
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
            sys.exit(1)
          else:
           print(f'{Fore.GREEN}\n[~] Numero: ', lol['number'])
           print('[~] Codigo del pais: ', lol['country_code'])
           print('[~] Nombre del pais: ', lol['country_name'])
           print('[~] Ubicacion: ', lol['location'])
           print('[~] Transportador: ', lol['carrier'])
           
       except Exception as e:
          print(f'{Fore.RED}\n[!] ERROR: {e}')
    # Abstract api
    if args.abstract:
       print(f'{Fore.BLUE}\n[~] Realizando escaneo con Abstract API...')
       time.sleep(2)

       url = f"https://phonevalidation.abstractapi.com/v1/?api_key={configuracion_dat['Abstract']}&phone={numero}"

       try:
          r = requests.get(url)
       except Exception as e:
          print(f"{Fore.RED}[!] ERROR: {e}")
          
       var = r.json()  
       if var["valid"] == False:
          print(f'\n{Fore.RED}[!] ERROR: El numero no es valido.')
       else:
        print(f'{Fore.GREEN}\n[~] Numero: {var["format"]["international"]}')
        print(f'{Fore.GREEN}[~] Codigo de pais: {var["country"]["code"]}')
        print(f'{Fore.GREEN}[~] Pais: {var["country"]["name"]}')
        print(f'{Fore.GREEN}[~] Ubicacion: {var["location"]}')
        print(f'{Fore.GREEN}[~] Tipo de linea: {var["type"]}')
        print(f'{Fore.GREEN}[~] Transportador: {var["carrier"]}')
    # --- VeriPhone
    if args.veriphone:
        print(f'{Fore.BLUE}\n[~] Realizando escaneo con VeriPhone...')
        time.sleep(2)
        pag = f"https://api.veriphone.io/v2/verify?phone={numero}&key={configuracion_dat['VeriPhone']}"
        
        try:
            r = requests.get(pag)
        except Exception as e:
            print(f"{Fore.RED}[!] ERROR: {e}")
    
        var = r.json()
        if var["phone_valid"] == False:
             print(f'\n{Fore.RED}[!] ERROR: El numero no es valido.')
        else:
             print(f'{Fore.GREEN}\n[~] Numero: {var["format"]["international"]}')
             print(f'[~] Tipo de linea: {var["phone_type"]}')
             print(f'[~] Región del teléfono: {var["phone_region"]}')
             print(f'[~] Pais: {var["country"]}')
             print(f'[~] Codigo de pais: {var["country_code"]}')
             print(f'[~] Formato internacional: {var["international_number"]}')
             print(f'[~] Formato local: {var["local_number"]}')
             print(f'[~] Transportador: {var["carrier"]}')
    # -- Phonenumbers
    if args.phonenumbers:
       print(f'{Fore.BLUE}\n[~] Realizando escaneo con PhoneNumbers...')
       time.sleep(2)

       phone = phonenumbers.parse(numero)
       international = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
       countrycode = international.split(' ')[0]
       country = geocoder.country_name_for_number(phone, 'en')
       location = geocoder.description_for_number(phone, 'en')
       carrierr = carrier.name_for_number(phone, 'en')

       print(f'\n{Fore.GREEN}[~] Formato internacional: {international}')
       print(f'[~] Nombre del país: {country} ({countrycode})')
       print(f'[~] Ciudad / Provincia: {location}')
       print(f'[~] Transportador: {carrierr}')
       for tiempo in timezone.time_zones_for_number(phone):
            print(f'[~] Zona horaria: {tiempo}')
            print('\n[~] Escaneo completo.')
    # Opencage
    if args.opencage:
        print(f'{Fore.BLUE}\n[~] Realizando escaneo con Opencage...')
        time.sleep(2)

        geo = OpenCageGeocode(configuracion_dat['OpencageKey'])
        num = phonenumbers.parse(numero)
        location = geocoder.description_for_number(num, 'en')
        query = str(location)
        results = geo.geocode(query)

        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']

        print(f'\n{Fore.GREEN}[~] Municipio: {location}')
        print(f'[~] Latitud: {lat}')
        print(f'[~] Longitud: {lng}')
    # Phonenumbers
    if args.phoneinfoga:
        print(f'{Fore.BLUE}\n[~] Realizando escaneo con Phoneinfoga...')
        time.sleep(2)

        subprocess.run(["./phoneinf/phoneinfoga", "scan", "-n", f"{numero}"])
    # Dorking
    if args.dork:
        print(f'{Fore.BLUE}\n[~] Realizando escaneo con Google dorking...')
        valor_entero = args.dork
        dom = ["com","com.tw","co.in","be","de","co.uk","co.ma","dz","ru","ca"]
        tld = random.choice(dom)
        dork_list = [f"intext:{numero}", f"intext:{numero} filetype:pdf", f"site:facebook.com intext:{numero}", f"site:twitter.com intext:{numero}", f"site:instagram.com intext:{numero}"]
        
        for dorks in dork_list:
            resultados = search(dorks, tld, num=valor_entero, stop=valor_entero, pause=valor_entero)
            for resultados_obtenidos in resultados:
               print(f'{Fore.GREEN}\n[ ✔  ] Busqueda encontrada!: {resultados_obtenidos}')

if args.numero:
    scan()
else:
       print(f'''{Fore.RED}[!] ERROR: Debes agregar algun argumento de escaneo: 
             
      -phoneinfoga          Añadir escaneo de la tool phoneinfoga.
      -phonenumbers         Añadir escaneo de la libreria phonenumbers.
      -numverify            Añadir escaneo de numverify.
      -opencage             Añadir escaneo con opencage.
      -abstract             Añadir escaneo con abstract api.
      -veriphone            Añadir escaneo con VeriPhone.
      -dork                 Añadir escaneo con google dorking.
       ''')
