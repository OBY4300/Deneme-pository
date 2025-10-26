# Metni tersine çeviren fonksiyon
def reverse_string(s):
	s_liste = []
	s_ters = ""
	son_j = 0
	
	str(s)
	for char in s:
		s_ters = char + s_ters
	return s_ters


# Programın ana fonksiyonu
def main():
	# Kullanıcıdan ters çevirmek için bir metin girmesini isteyin
	user_input = input("Ters çevirmek istediğiniz metni girin: ")
	# Kullanıcının girdi metnini reverse_string fonksiyonuna gönderin
	# Ters çevrilmiş metni yazdırın
	print("Ters çevrilmiş metin:", reverse_string(user_input))


# Programın doğrudan çalıştırıldığını, modül olarak içe aktarılmadığını kontrol edin
if __name__ == "__main__":
	main()  # Program doğrudan çalıştırıldıysa ana fonksiyon çağrılır
