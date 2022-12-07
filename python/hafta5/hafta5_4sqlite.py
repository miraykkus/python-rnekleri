import sqlite3
bag = sqlite3.connect("a.vt")
cursor = bag.cursor()
#cursor veritabanı üstünde işlem yapmak için kullınılcak imleç
cursor.execute("CREATE TABLE IF NOT EXISTS kitap"
               "(id INTEGER NOT NULL PRIMARY KEY,"
               "isim TEXT, yazar TEXT, yayinevi TEXT,"
               "sayfasayisi INT)")
bag.commit()
bag.close()#bağlantıyı kopardık