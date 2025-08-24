 <template>
      <div class="container mx-auto p-4 md:p-8">
        <h1 class="text-3xl font-bold mb-6 text-gray-800">Lista de Pokémon</h1>
        <input
          v-model="searchKeyword"
          placeholder="Buscar por nombre..."
          @input="fetchPokemons"
          class="p-3 border border-gray-300 rounded-lg w-full md:w-1/3 mb-6 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />

        <div class="bg-white shadow-md rounded-lg overflow-hidden">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ID</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Nombre</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Experiencia Base</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Altura</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Peso</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="pokemon in pokemons" :key="pokemon.id" @click="selectPokemon(pokemon.id)" class="hover:bg-gray-100 cursor-pointer transition duration-150 ease-in-out">
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ pokemon.id }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ pokemon.name }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ pokemon.base_experience }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ pokemon.height }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ pokemon.weight }}</td>
              </tr>
              <tr v-if="pokemons.length === 0">
                <td colspan="5" class="px-6 py-4 text-center text-sm text-gray-500">No se encontraron Pokémon.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div v-if="selectedPokemon" class="mt-8 bg-white shadow-lg rounded-lg p-6 md:p-8 border-l-4 border-blue-500">
          <h2 class="text-2xl font-bold mb-4 text-gray-800">Detalles de {{ selectedPokemon.name }}</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <p class="text-gray-700"><strong class="font-semibold">ID:</strong> {{ selectedPokemon.id }}</p>
              <p class="text-gray-700"><strong class="font-semibold">Nombre:</strong> {{ selectedPokemon.name }}</p>
              <p class="text-gray-700"><strong class="font-semibold">Experiencia Base:</strong> {{ selectedPokemon.base_experience }}</p>
              <p class="text-gray-700"><strong class="font-semibold">Altura:</strong> {{ selectedPokemon.height }}</p>
              <p class="text-gray-700"><strong class="font-semibold">Peso:</strong> {{ selectedPokemon.weight }}</p>
            </div>
          </div>
        </div>
      </div>
    </template>

    <script setup>
    import { ref, onMounted } from 'vue';

    const pokemons = ref([]);
    const selectedPokemon = ref(null);
    const searchKeyword = ref('');

    const API_BASE_URL = 'http://127.0.0.1:8000';

    const fetchPokemons = async () => {
      let url = `${API_BASE_URL}/pokemons`;
      if (searchKeyword.value) {
        url = `${API_BASE_URL}/pokemons/search/?keyword=${searchKeyword.value}`;
      }

      try {
        const response = await fetch(url);
        console.log('Respuesta cruda de la API:', response); 
        if (!response.ok) {
            throw new Error(`Error HTTP! Estado: ${response.status}`);
        }
        const data = await response.json();
        console.log('Datos JSON parseados:', data);
      } catch (error) {
        console.error('Error al obtener los Pokémon:', error);
        pokemons.value = [];
      }
    };

    onMounted(() => {
      fetchPokemons();
    });
    </script>
