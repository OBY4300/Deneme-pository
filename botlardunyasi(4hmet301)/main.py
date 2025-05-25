import discord
from discord.ext import commands
from config import token
from logic import Pokemon, pokemongo, pokemon2
from buyukharf import ilkibuyuk

global pokemonis2
pokemonis2 = False

# Bot için yetkileri/intents ayarlama
intents = discord.Intents.default()  # Varsayılan ayarların alınması
intents.messages = True              # Botun mesajları işlemesine izin verme
intents.message_content = True       # Botun mesaj içeriğini okumasına izin verme
intents.guilds = True                # Botun sunucularla çalışmasına izin verme

# Tanımlanmış bir komut önekine ve etkinleştirilmiş amaçlara sahip bir bot oluşturma
bot = commands.Bot(command_prefix='!', intents=intents)

# Bot çalışmaya hazır olduğunda tetiklenen bir olay
@bot.event
async def on_ready():
	print(f'main.py üzerinden giriş yapıldı: {bot.user.name}')  # Botun adını konsola çıktı olarak verir

# '!go' komutu
@bot.command()
async def go(ctx):
	global pokemonis2
	author = ctx.author.name  # Mesaj yazarının adını alma
	# Kullanıcının zaten bir Pokémon'u olup olmadığını kontrol edin. Eğer yoksa, o zaman...
	if author not in Pokemon.pokemons.keys():
		pokemon = Pokemon(author)  # Yeni bir Pokémon oluşturma
		await ctx.send(await pokemon.info())  # Pokémon hakkında bilgi gönderilmesi
		image_url = await pokemon.show_img()  # Pokémon resminin URL'sini alma
		if image_url:
			name=await pokemon.get_name()
			embed = discord.Embed(title=ilkibuyuk(name))  # Gömülü mesajı oluşturma
			embed.set_image(url=image_url) # Pokémon'un görüntüsünün ayarlanması
			boy=pokemon.height * 10
			kilo=pokemon.weight / 10
			embed.add_field(name="Boy",value=boy,inline=True)
			embed.add_field(name="Kilo",value=kilo,inline=True) 
			await ctx.send(embed=embed)  # Görüntü içeren gömülü bir mesaj gönderme
			pokemonis2 = False
		else:
			await ctx.send("Pokémonun görüntüsü yüklenemedi!")
	else:
		if pokemonis2 == False:
			pokemon2 = Pokemon(author)  # Yeni bir Pokémon oluşturma
			await ctx.send(await pokemon2.info())  # Pokémon hakkında bilgi gönderilmesi
			image_url = await pokemon2.show_img()  # Pokémon resminin URL'sini alma
			if image_url:
				name=await pokemon2.get_name()
				embed = discord.Embed(title=ilkibuyuk(name))  # Gömülü mesajı oluşturma
				embed.set_image(url=image_url) # Pokémon'un görüntüsünün ayarlanması
				boy=pokemon2.height * 10
				kilo=pokemon2.weight / 10
				embed.add_field(name="Boy",value=boy,inline=True)
				embed.add_field(name="Kilo",value=kilo,inline=True) 
				await ctx.send(embed=embed)  # Görüntü içeren gömülü bir mesaj gönderme
				pokemonis2 = True
		else:
			await ctx.send("Zaten kendi Pokémonlarınızı oluşturdunuz!")  # Bir Pokémon'un daha önce oluşturulup oluşturulmadığını gösteren bir mesaj

@bot.command()
async def savas(ctx):
	if pokemongo == True and pokemon2 != None:
		await ctx.send("Savaş başladı!")
		await ctx.send("Birinci oyuncu hangi hareketi kullanacak?")
		


bot.run(token)