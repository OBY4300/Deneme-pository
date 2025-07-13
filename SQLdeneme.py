import sqlite3 
con = sqlite3.connect("tutorial.db") # veri tabanına bağlantı, eğer veri tabanı yoksa dosya oluşturulacaktır.

cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS movie")
cur.execute("CREATE TABLE movie(title text, year integer, score real NOT NULL)")
#NOT NULL boş bırakılamaz demek.
#ve argümanların yanındaki veri tipleri ise static şekilde
#yazılmış açıklayıcılar.
data = [
        ("A", 1982, 7.9),
        ("B", 1983, 7.5),
        ("C", 1979, 8.0),
    ]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)

cur.execute("INSERT INTO movie (title, year,score) VALUES ('Z', 2014,6.0)")
con.commit()
for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)

con.close()