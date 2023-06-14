from pymongo import MongoClient
from datetime import datetime

# Configuración de la conexión a MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['ExploreCheck']
users_collection = db['users']
places_collection = db['lugares']
checkins_collection = db['Check']

# Obtener el nombre de usuario y el nombre del lugar desde la entrada
username = input("Nombre de usuario: ")
place_name = input("Nombre del lugar: ")

# Buscar el usuario y el lugar por nombre
user = users_collection.find_one({'username': username})
place = places_collection.find_one({'nombre': place_name})

# Verificar si el usuario y el lugar existen
if not user or not place:
    print('Usuario o lugar no encontrado')
    exit()

# Lista de opciones
opciones = ['1 Estrella', '2 Estrellas', '3 Estrellas', '4 Estrellas', '5 Estrellas']

# Solicitar al usuario que seleccione una opción
opcion_seleccionada = int(input("Selecciona una opción (1-5): "))

# Validar la opción seleccionada
if opcion_seleccionada in range(1, 6):
    opcion = opciones[opcion_seleccionada - 1]
    print("Opción seleccionada:", opcion)
else:
    print("Opción inválida. Debes seleccionar un número del 1 al 5.")



comentario = input("Ingrese su comentario: ")



# Crear un nuevo check-in o actualizar uno existente
existing_checkin = checkins_collection.find_one({'userId': user['_id'], 'placeId': place['_id']})
if existing_checkin:
    # Actualizar un check-in existente
    update_result = checkins_collection.update_one(
        {'_id': existing_checkin['_id']},
        {'$set': {'user': user, 'place': place}}
    )
    print('Check-in actualizado:', update_result.modified_count)
else:
    # Crear un nuevo check-in
    new_checkin = {
        'userId': user['_id'],
        'placeId': place['_id'],
        'user': username,
        'place': place_name,
	'Estrellas': opcion,
	'comentario': comentario,
        'date': datetime.now(),
    }
    insert_result = checkins_collection.insert_one(new_checkin)
    print('Nuevo check-in creado:', insert_result.inserted_id)

# Cerrar la conexión a MongoDB
client.close()
