

from glpi import GLPI
import requests, json



baseUrl = "https://ingeproserv.cl/camiones"#https://appmarketplace.iconstruye.com/rest.aspx?query=topo
url = baseUrl + '/apirest.php/initSession'
auth = ('rsilcas', 'rsilcas')
headers = {'App-Token': '0T22iu8HaZSNtGBqGwXzOPhIynbkJT2CeyDctDyA',
           'Content-Type': 'application/json'}
a = requests.get(url, auth=auth, headers=headers)
elRegistro = {'input': {'name': 'Camion Extraccion Caterpillar 797F N23', 'serial': 'N23', "manufacturers_id":"1", "computertypes_id":"3", "computermodels_id":"1"}}
print (str(a))

respuestaLogin = json.loads(a.text)
print("respuestaLogin:" + str(respuestaLogin))
token = respuestaLogin['session_token']
print("TOKEN:" + token)

headers = { 'Authorization' : 'Token ' + token , 'App-Token': '0T22iu8HaZSNtGBqGwXzOPhIynbkJT2CeyDctDyA', 'Session-Token': token}

b = requests.post(baseUrl + '/apirest.php/Computer', json=elRegistro, headers=headers)


respuestaRegistro = json.loads(b.text)
idCreado = respuestaRegistro['id']

#COMENTAR ESTO
#idCreado = 1

print (str(b))
print ("-----------------------------------SEPARADOR-----------------------------------------------")

print (str(b.text))
print ("-----------------------------------SEPARADOR-----------------------------------------------")
print("respuestaRegistro:idCreado:" + str(idCreado))


rest_post_lectura = requests.get(baseUrl + '/apirest.php/Computer/' +  str(idCreado), headers=headers)


respuestaLectura = json.loads(rest_post_lectura.text)
print ("-----------------------------------SEPARADOR-----------------------------------------------")
print (str(rest_post_lectura.text))

print ("-----------------------------------SEPARADOR-----------------------------------------------")


print("respuestaLectura:idCreado:" + str(respuestaLectura))

print ("-----------------------------------SEPARADOR FINAL-----------------------------------------------")

#admin
#Camiones123!


#USER https://forum.glpi-project.org/login.php
#Username: rsilcas
#Password: LrErunqOhU0F


#AYUDAS
#https://forum.glpi-project.org/viewtopic.php?id=158163
#https://fossies.org/dox/glpi-9.5.3/md_apirest.html
#https://opengear.zendesk.com/hc/en-us/articles/115003549186-How-do-I-authenticate-to-your-RESTful-API-

#GLPI EN PYTHON #pip install glpi
#https://forum.glpi-project.org/viewtopic.php?id=164887

#SE DEBE OTORGAR PERMISOS A LA IP CON LA QUE SALE LA MAQUINA
#                          https://www.cual-es-mi-ip.net/

#DOCUMENTACION
#                          https://ingeproserv.cl/camiones/apirest.php/

#OBTENER ESTO DESDE LA APP
#Token personal            SrUKxgZwDA9e3826vrXz3Pdkyf5IawlmOownALEf

#API token                 Twp9bUZJsp775JSVQSeEzDNY7APtIOx1wo2qlZho


#admin
#Camiones123!



"""
hi

in this code:
--------------------------------
from glpi import GLPI
import requests
url = 'https://hd.integrasky.ru/apirest.php/initSession'
auth = ('username', 'password')
headers = {'App-Token': 'token',
           'Content-Type': 'application/json'}
requests.get(url, auth=auth, headers=headers)  #this GET is when you obtain the token, but you are losing the token, you need to save in a STRING to use in the next line in a HEADER of the POST
----------------------------------------------------


in this line you need to add the token of the last line
----------------------------------------------------
requests.post('http://hd.integrasky.ru/apirest.php/Ticket', json=payload)
----------------------------------------------------

i am in this code in this moment, if i win, i will show you

"""


print("fin")