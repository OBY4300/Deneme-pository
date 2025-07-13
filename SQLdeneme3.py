import sqlite3 

# Veri tabanı dosyasını açma
con = sqlite3.connect('marvel.db')

# Tablo oluşturma
with con:
    con.execute("""
        CREATE TABLE marvel (
            ID INTEGER PRIMARY KEY,
            name TEXT,
            superpower TEXT,
            status TEXT
);
    """)
    
# Bir tablonun silinmesi
with con:
    con.execute("DROP TABLE marvel")

# Bu tabloya girişler eklemek için şu adımları gerçekleştirmemiz gerekiyor.

# Sorguyu hazırlama
sql = 'INSERT INTO marvel (ID, name, superpower, status) values(?, ?, ?, ?)'

# Sorgu için veri tanımlama
data = [
    (1, 'Hulk', 'İnsanüstü güç', 'İyi'),
    (2, 'Thor', 'Mjölnir', 'İyi'),
]

# İteratif sorgu kullanarak tüm verileri bir kerede ekleme
with con:
    con.executemany(sql, data)
# Aşağıdaki komutu kullanarak kaydı güncelleyin:

isim = input("Hangi kahraman? ")

durum = input("Durumu nedir? ")



# Hulk'un durumunu güncelleme
with con:
    con.execute("UPDATE marvel SET status = ? WHERE name = ?",durum, isim)
# Tablodan bir girişi silmek için aşağıdaki komutu kullanın:

# Thor ile ilgili girişi silme
with con:
    con.execute("DELETE FROM marvel WHERE name = ?",('Thor',))