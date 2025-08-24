uvicorn main:app --reload // comando manualmente para levantar la api

http://127.0.0.1:8000/

http://127.0.0.1:8000/pokemons

http://127.0.0.1:8000/pokemons/1

http://127.0.0.1:8000/pokemons/search/?keyword=bulbasaur // direcciones de acceso para la api desde navegador

kitsune-project\fronted\vue-project>npm run dev // ejecucion veu para listar pokemon de la base en la tabla web






En este proyecto se utiliza la api de pokemon, gracias a que fue la unica que me estaba funcionando a estas horas.

para poder ejecutar este proyecto necesitamos primero crear la base de datos de la Sigueinte informacion 

CREATE DATABASE pokemondb;

USE pokemondb;

CREATE TABLE pokemons (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    base_experience INT,
    height INT,
    weight INT
);

una vez creada la base de datos y la tabla correspondiente procedemos a ejecutar la etl
para poder acceder a la api de pokemon y guardar los datos escigidos en la base de datos

python etl.py //comando para ejecutar el etl hay que tener en cuenta que se deve estar en la carpeta etl 

![Image_Alt](https://github.com/faridgomez/Consumo-de-API/blob/c7011ad02192ef87847c40cd0e1d962eeafbec0b/IMG/ejecucion%20etl.png)


Despues de realizar este paso la base de datos se nos llenara con la siguiente informacion



el siguiente paso es levantar los servios de la api "uvicorn main:app --reload" // comando manualmente para levantar la api dentro de la carpeta api para ejecutar esté script 





y si accedemos a las siguientes rutas nos deve aparecer informacion como esta:

http://127.0.0.1:8000/

http://127.0.0.1:8000/pokemons

http://127.0.0.1:8000/pokemons/1

http://127.0.0.1:8000/pokemons/search/?keyword=bulbasaur 








y ya por ultimo el front del app el cujal es ta con VUE kitsune-project\fronted\vue-project>npm run dev // ejecucion veu para listar pokemon de la base en la tabla web 
