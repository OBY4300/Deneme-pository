import aiohttp
async def get_name(self):
		# PokeAPI üzerinden Pokémon adını almak için eşzamansız/asenkron metot
		url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API
		async with aiohttp.ClientSession() as session:  # HTTP oturumu açma
			async with session.get(url) as response:  # GET isteği gönderme
				if response.status == 200:
					data = await response.json()  # JSON yanıtının alınması ve çözümlenmesi
					return data['forms'][0]['name']  # Pokémon adını döndürme
				else:
					return "Pikachu"  # İstek başarısız olursa varsayılan adı döndürür