// Función para agregar un amigo a un usuario
function agregarAmigo(username, amigo) {
    fetch('/agregarAmigo', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, amigo })
    })
    .then(response => response.json())
    .then(data => {
        console.log(`${data.amigo} agregado como amigo de ${data.username}`);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Función para obtener la lista de amigos de un usuario
function obtenerAmigos(username) {
    fetch(`/obtenerAmigos?username=${username}`)
    .then(response => response.json())
    .then(data => {
        console.log(`Amigos de ${data.username}:`);
        data.amigos.forEach(amigo => {
            console.log(amigo);
        });
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Función para actualizar el nombre de un amigo de un usuario
function actualizarNombreAmigo(username, amigo, nuevoNombre) {
    fetch('/actualizarNombreAmigo', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, amigo, nuevoNombre })
    })
    .then(response => response.json())
    .then(data => {
        console.log(`Nombre de ${data.amigo} actualizado a ${data.nuevoNombre} para ${data.username}`);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Función para eliminar un amigo de un usuario
function eliminarAmigo(username, amigo) {
    fetch('/eliminarAmigo', {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, amigo })
    })
    .then(response => response.json())
    .then(data => {
        console.log(`${data.amigo} eliminado como amigo de ${data.username}`);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Ejemplo de uso
const username = 'Moranciox';
const amigo = 'Juan';

agregarAmigo(username, amigo);
obtenerAmigos(username);
const nuevoNombre = 'Juan Pérez';
actualizarNombreAmigo(username, amigo, nuevoNombre);
eliminarAmigo(username, amigo);

