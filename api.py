#API REST
#URL - https://google.com/fotos
#Metodos - GET (OBTENER INFORMACION), POST(MANDAR INFORMACION PARA GUARDAR)
#Body - el metodo get no recibe body porque va directamente en la url
#pero en el metodo post y put si se envia un body (un json)
#PUT/PATCH (MODIFICAR ALGO QUE YA EXISTE), DELETE(ELIMINAR)
#encabezados AUTHENTICATION: https://bEARER XXX-123456
#path parameters son parametros de la url https://google.com/fotos/1/
#query params https://google.com/fotos?q=python


#para poder consumir apis necesitamos el requests
#pip install requests
import requests
response= requests.get('https://www.breakingbadapi.com/api/character/random')
print(response.json())#obtiene el objeto y lo parsea a un diccionario 
personaje= response.json()[0]
print(personaje['name'])
print(personaje['birthday'])