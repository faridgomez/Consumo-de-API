from fastapi import FastAPI, HTTPException
import mysql.connector
import os
from fastapi.middleware.cors import CORSMiddleware # Importa el middleware CORS

# Detalles de la conexión a la base de datos MySQL local
# ¡IMPORTANTE! Reemplaza con tu usuario y contraseña de MySQL
DB_HOST = "localhost"
DB_USER = "root" # <-- Asegúrate de que este usuario es correcto
DB_PASSWORD = "" # <-- Asegúrate de que esta contraseña es correcta
DB_NAME = "pokemondb"

def get_db_connection():
    """
    Retorna una conexión a la base de datos MySQL local.
    """
    try:
        return mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        # Aquí podrías lanzar una HTTPException si la conexión es crítica
        raise HTTPException(status_code=500, detail="Error de conexión a la base de datos")

app = FastAPI()

# Configuración de CORS para permitir solicitudes desde tu frontend
# Estos son los ORÍGENES EXACTOS desde donde tu frontend se puede conectar
origins = [
    "http://localhost",           # Para http://localhost (sin puerto específico)
    "http://localhost:5173",      # El puerto común de desarrollo de Vue
    "http://127.0.0.1:5173",      # La IP loopback con el puerto de Vue
    "http://127.0.0.1:8000",      # A veces es necesario si la API se llama a sí misma
    "http://localhost:80",        # Si el frontend se sirve en el puerto 80 (por ejemplo, con Nginx en Docker)
    "http://127.0.0.1:80",        # La IP loopback para el puerto 80
    # Si tu frontend se ejecuta en un puerto diferente (ej. 3000, 8080), agrégalo aquí:
    # "http://localhost:3000",
    # "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # Lista de orígenes permitidos
    allow_credentials=True,         # Permite cookies/credenciales de origen cruzado
    allow_methods=["*"],            # Permite todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],            # Permite todas las cabeceras
)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Pokémon"}

@app.get("/pokemons") # Ruta para listar todos los Pokémon
def get_all_pokemons():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pokemons")
    pokemons = cursor.fetchall()
    cursor.close()
    db.close()
    return {"pokemons": pokemons} # Devuelve los datos bajo la clave 'pokemons'

@app.get("/pokemons/{pokemon_id}") # Ruta para consultar un Pokémon por ID
def get_pokemon_by_id(pokemon_id: int):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pokemons WHERE id = %s", (pokemon_id,))
    pokemon = cursor.fetchone()
    cursor.close()
    db.close()
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokémon no encontrado")
    return {"pokemon": pokemon} # Devuelve el dato bajo la clave 'pokemon'

@app.get("/pokemons/search/") # Ruta para filtrar por palabra clave en el nombre
def search_pokemons(keyword: str):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM pokemons WHERE name LIKE %s"
    cursor.execute(query, (f"%{keyword}%",))
    pokemons = cursor.fetchall()
    cursor.close()
    db.close()
    return {"pokemons": pokemons} # Devuelve los datos bajo la clave 'pokemons'
