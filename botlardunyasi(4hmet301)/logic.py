import aiohttp  # Eşzamansız HTTP istekleri için bir kütüphane
import random

pokemongo = False
pokemon2 = None

class Pokemon:
	pokemons = {}
	# Nesne başlatma (kurucu)
	def __init__(self, pokemon_trainer):
		self.pokemon_trainer = pokemon_trainer
		self.pokemon_number = random.randint(1, 1000)
		self.name = None
		self.height = None
		self.weight = None
		if pokemon_trainer not in Pokemon.pokemons:
			Pokemon.pokemons[pokemon_trainer] = self
		else:
			self = Pokemon.pokemons[pokemon_trainer]

	async def get_name(self):
		# PokeAPI aracılığıyla bir pokémonun adını almak için asenktron metot
		url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API
		async with aiohttp.ClientSession() as session:  #  HTTP oturumu açma
			async with session.get(url) as response:  # GET isteği gönderme
				if response.status == 200:
					data = await response.json()  # JSON yanıtının alınması ve çözümlenmesi
					return data['forms'][0]['name']  #  Pokémon adını döndürme
				else:
					return "Pikachu"  # İstek başarısız olursa varsayılan adı döndürür
	async def load_data(self):
		# PokeAPI aracılığıyla bir pokémonun adını almak için asenktron metot
		url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API
		async with aiohttp.ClientSession() as session:  #  HTTP oturumu açma
			async with session.get(url) as response:  # GET isteği gönderme
				if response.status == 200:
					data = await response.json()
					self.height=data["height"]
					self.weight=data["weight"]
	async def info(self):
		# Pokémon hakkında bilgi döndüren bir metot
		if not self.name:
			self.name = await self.get_name() 
		await self.load_data()
		pokemongo = True
		return (f"Pokémonunuzun ismi: {self.name}\nPokemonun boyu: {self.height*10} santim\nPokemonun kilosu: {self.weight/10} kilogram.")  # Pokémon adını içeren dizeyi döndürür

	async def show_img(self):
		url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API
		async with aiohttp.ClientSession() as session:  #  HTTP oturumu açma
			async with session.get(url) as response:  # GET isteği gönderme
				if response.status == 200:
					data = await response.json()
					img_url = data['sprites']['front_default']
					return img_url
