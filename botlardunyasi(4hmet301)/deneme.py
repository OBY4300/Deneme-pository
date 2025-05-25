import json

bilgi_mesaji = {"echo": "false", "giriş_işleme": "true"}
print('"echo": ' + bilgi_mesaji["echo"] + "," + " " + '"giriş_işleme": ' + bilgi_mesaji["giriş_işleme"])

bilgi_mesaji = open("../botlardunyasi(4hmet301)/bilgi_mesaji.json", "r")
JSONbilgi = json.load(bilgi_mesaji)
print(type(JSONbilgi))
print('"echo": ' + JSONbilgi["echo"] + "," + " " + '"giriş_işleme": ' + JSONbilgi["giriş_işleme"])



def info():
	bilgi_mesaji = {"echo": "false", "giriş_işleme": "true"}
	print('"echo": ' + bilgi_mesaji["echo"] + "," + " " + '"giriş_işleme": ' + bilgi_mesaji["giriş_işleme"])

def mesaji_yukle():
	with open("bilgi_mesaji.json", "r") as f:
		return json.load(f)

"""
def mesaji_kaydet():
    with open("bilgi_mesaji.json", "w") as f:
        json.dump(bilgi_mesaji)
"""
def ayar(anahtar: str, deger: str):
	bilgi_mesaji = mesaji_yukle()
	

	# Sadece "true" veya "false" kabul edilsin
	if deger.lower() not in ["true", "false"]:
		print('Lütfen sadece "true" veya "false" yazın.')
		return None

	# Anahtar geçerli mi?
	if anahtar in bilgi_mesaji:
		dict(bilgi_mesaji)
		eski = bilgi_mesaji[anahtar]
		bilgi_mesaji[anahtar] = deger.lower()
		print(f'"{anahtar}" güncellendi: "{eski}" -> "{deger.lower()}"')
		print(bilgi_mesaji)
		#Değiştirilen değerleri kaydetme:
		JSONdump = open("../bilgi_mesaji.json", "w")
		JSONdump.write(json.dumps(bilgi_mesaji))
	else:
		print(f'"{anahtar}" geçerli bir anahtar değil. Geçerli anahtarlar: {", ".join(bilgi_mesaji.keys())}')
		
mesaji_yukle()

info()

ayar("giriş_işleme", "false")

#mesaji_kaydet()