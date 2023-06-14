from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['ExploreCheck']
users_collection = db['users']

def agregar_amigo(username, amigo):
    users_collection.update_one(
        {'username': username},
        {'$addToSet': {'amigos': amigo}}
    )
    print(f'{amigo} agregado como amigo de {username}')

def obtener_amigos(username):
    usuario = users_collection.find_one({'username': username})
    amigos = usuario.get('amigos', [])
    print(f'Amigos de {username}:')
    for amigo in amigos:
        print(amigo)

def actualizar_nombre_amigo(username, amigo, nuevo_nombre):
    users_collection.update_one(
        {'username': username, 'amigos': amigo},
        {'$set': {'amigos.$': nuevo_nombre}}
    )
    print(f'Nombre de {amigo} actualizado a {nuevo_nombre} para {username}')

def eliminar_amigo(username, amigo):
    users_collection.update_one(
        {'username': username},
        {'$pull': {'amigos': amigo}}
    )
    print(f'{amigo} eliminado como amigo de {username}')

username = 'Moranciox'
amigo = 'Juan'

agregar_amigo(username, amigo)
obtener_amigos(username)
nuevo_nombre = 'Juan Pérez'
actualizar_nombre_amigo(username, amigo, nuevo_nombre)
eliminar_amigo(username, amigo)

client.close()
