import discord
from discord.ext import commands
from config import token
import json
import sys

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)

def mesaji_kaydet(veri):
    with open("/Users/orhanberk/Desktop/botlardunyasi(4hmet301)/bilgi_mesaji.json", "w") as f:
        json.dump(veri, f)

def mesaji_yukle():
    with open("/Users/orhanberk/Desktop/botlardunyasi(4hmet301)/bilgi_mesaji.json", "r", encoding="utf-8") as f:
        return json.load(f)

def echho():
    bilgi_mesaji = mesaji_yukle()
    if bilgi_mesaji["echo"] == "true":
        async def on_message(message):
            await message.channel.send(message.content)

@client.event
async def on_ready():
    print(f"{client.user} olarak giriş yaptık.")

@client.event
async def on_message(message):
    bilgi_mesaji = mesaji_yukle()
    if message.author == client.user:
        return
    if message.content.startswith(client.command_prefix):
        if bilgi_mesaji["giriş_işleme"] == "true":
            await client.process_commands(message)
        else:
            pass
    else:
        if bilgi_mesaji["echo"] == "true":
            await message.channel.send(message.content)
        

@client.command()
async def about(ctx):
    await ctx.send("4hmet301, ailede 3.")
    
@client.command()
async def merhaba(ctx):
    await ctx.send("merhaba...")

@client.command()
async def info(ctx):
	bilgi_mesaji = mesaji_yukle()
	await ctx.send("{" + '"echo": ' + '"' + bilgi_mesaji["echo"] + '"' + "," + " " + '"giriş_işleme": ' + '"' + bilgi_mesaji["giriş_işleme"] + '"' + "}")

@client.command()
async def sessionend(ctx):
    await ctx.send("görüşürüz...")
    sys.exit(0)

@client.command()
async def ayar(ctx, anahtar: str, deger: str):
    bilgi_mesaji = mesaji_yukle()

    if deger.lower() not in ["true", "false"]:
        await ctx.send('sadece "true" veya "false" yaz.')
        return

    if anahtar in bilgi_mesaji:
        eski = bilgi_mesaji[anahtar]
        bilgi_mesaji[anahtar] = deger.lower()
        mesaji_kaydet(bilgi_mesaji)
        await ctx.send(f'"{anahtar}" güncellendi: "{eski}" -> "{deger.lower()}"')
    else:
        await ctx.send(f'"{anahtar}" geçerli bir ayar değil. Mevcut ayarlar: {", ".join(bilgi_mesaji.keys())}')

@client.command()
async def yaşasın(ctx):
    await ctx.send("eveeet...")

client.run(token)