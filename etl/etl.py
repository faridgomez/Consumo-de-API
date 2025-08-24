import requests
import mysql.connector


db_connection = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="",
    database="pokemondb"
)
cursor = db_connection.cursor()

def fetch_and_save_pokemons():
    # Extraer datos de la API de PokeAPI (los primeros 20 pokemons)
    url = "https://pokeapi.co/api/v2/pokemon"
    response = requests.get(url)
    data = response.json()
    
    
    for pokemon in data['results']:
        pokemon_name = pokemon['name']
        details_url = pokemon['url']
        details_response = requests.get(details_url)
        details_data = details_response.json()

        # Normalizar
        poke_id = details_data['id']
        base_experience = details_data.get('base_experience', 0)
        height = details_data.get('height', 0)
        weight = details_data.get('weight', 0)

        insert_query = """
        INSERT INTO pokemons (id, name, base_experience, height, weight)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        name = VALUES(name), base_experience = VALUES(base_experience), height = VALUES(height), weight = VALUES(weight);
        """
        data_to_insert = (poke_id, pokemon_name, base_experience, height, weight)
        cursor.execute(insert_query, data_to_insert)

    db_connection.commit()
    print("Datos de Pokémon guardados exitosamente.")


fetch_and_save_pokemons()

# Cerrar la conexión
cursor.close()
db_connection.close()