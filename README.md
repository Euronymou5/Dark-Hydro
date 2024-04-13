# Dark-Hydro

Dark-Hydro es una herramienta de OSINT creada en Python con el objetivo de recopilar información sobre un número de teléfono utilizando APIs públicas y técnicas de Google Dorking.

Con Dark-Hydro es pobible obtener:

>- Codigo del pais_

> - Nombre del pais_

>- Ubicacion del numero de telefono (Ciudad)_

> - Transportador_

>- Latitud y Longitud_

>- Búsquedas de dorking archivos pdf, redes sociales, paginas web, donde el numero telefónico ha sido encontrado

## Configuracion

Antes de utilizarlo, es necesario configurar algunas claves API, entre las API:

- [Numverify](https://numverify.com)
- [Opencage](https://opencagedata.com)
- [Abstract API](https://www.abstractapi.com/api/phone-validation-api)
- [VeriPhone](https://veriphone.io)

Una vez obtenida nuestra clave API, es necesario colocar cada una en orden en el archivo `config.json` de la siguiente forma:

```json
{
    "OpencageKey": "ReemplazarPorApikeyOpencage",
    "Numverifykey": "ReemplazarPorApikeyNumverify",
    "Abstract": "ReemplazarPorApikeyAbstract",
    "VeriPhone": "ReemplazarPorApikeyVeriPhone"
}
```
## Instalacion

> Clonamos el repositorio.
````
git clone https://github.com/Euronymou5/Dark-Hydro
````

> Ejecutamos el instalador de las dependecias.
```
sudo bash install.sh
```

### Ejemplos de uso

> Mostrar ayuda.

```
python3 main.py -h
```
```
usage: main.py [-h] [-phoneinfoga] [-numero NUMERO] [-phonenumbers] [-numverify] [-opencage] [-abstract] [-veriphone]
               [-dork DORK]

options:
  -h, --help            show this help message and exit
  -phoneinfoga          Añadir escaneo de la tool phoneinfoga.
  -numero NUMERO, -n NUMERO
                        Agregar numero telefonico.
  -phonenumbers         Añadir escaneo de la libreria phonenumbers.
  -numverify            Agregar escaneo de numverify.
  -opencage             Agregar escaneo con opencage.
  -abstract             Agregar escaneo con abstract api.
  -veriphone            Agregar escaneo con VeriPhone.
  -dork DORK            Agregar escaneo con google dorks.
```


> Ejemplo de uso basico
```
    python3 main.py -n +19496660724 -phonenumbers
```
>Mas de una api en el escaneo
```
python3 main.py -n +19496660724 -veriphone -numverify -phoneinfoga
```
> Uso del argumento dork
```
python3 main.py -n +19496660724 -dork 15
```
El argumento "dork" recibe un valor entero, en este caso el número 15. Este número será la cantidad de resultados que nos dará al realizar un escaneo con Google Dorking sobre el número de teléfono.

**Aclaracion!**

A veces, no se mostrará ningún resultado utilizando el dorking, lo que indica que el número telefónico no ha sido encontrado en ningún sitio de internet.

## Imagenes

![image](https://github.com/Euronymou5/Dark-Hydro/assets/85043356/029821e2-db56-40a8-b7ea-d1c83c7a30e5)


## :globe_with_meridians: Contacto :globe_with_meridians:
[![discord](https://img.shields.io/badge/Discord-euronymou5-a?style=plastic&logo=discord&logoColor=white&labelColor=black&color=7289DA)](https://discord.com/users/452720652500205579)

![email](https://img.shields.io/badge/ProtonMail-mr.euron%40proton.me-a?style=plastic&logo=protonmail&logoColor=white&labelColor=black&color=8B89CC)

[![Twitter](https://img.shields.io/badge/Twitter-@Euronymou51-a?style=plastic&logo=twitter&logoColor=white&labelColor=black&color=1DA1F2)](https://twitter.com/Euronymou51)
