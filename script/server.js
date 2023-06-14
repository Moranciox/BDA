const express = require('express');
const app = express();
const MongoClient = require('mongodb').MongoClient;
const url = 'mongodb://localhost:27017'; // URL de conexión a MongoDB
const dbName = 'ExploreCheck'; // Nombre de tu base de datos

// Ruta para obtener los datos de la base de datos y enviarlos al HTML
app.get('/', (req, res) => {
    MongoClient.connect(url, { useUnifiedTopology: true }, (err, client) => {
        if (err) {
            console.error('Error al conectar a la base de datos:', err);
            return;
        }
        const db = client.db(dbName);
        const collection = db.collection('users'); // Reemplaza 'coleccion' por el nombre de tu colección

    // Realiza la consulta a la base de datos y obtén los datos que necesites
        collection.find({}).toArray((err, data) => {
            if (err) {
                console.error('Error al obtener los datos:', err);
                return;
            }
            res.send(data); // Envía los datos al cliente (HTML)
            client.close();
        });
    });
});

// Inicia el servidor en un puerto específico
app.listen(3000, () => {
    console.log('Servidor iniciado en el puerto 3000');
});
