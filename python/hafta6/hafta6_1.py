"""
1. veri isimli klasör oluştur
2. zip dosyasını veri klasörüne çıkart
3. zip dosyası içindeki csv dosyalarının tüm içeriğini tek bir csvde birlrştir. volume olmasın
4. kayıtların tamamını sqlite veritabanına tablo oluşturarak yükle
5. kullanıcının belirlediği paritenin, aralığın, değerin grafiğini çizdir
"""

import os
import zipfile
import pandas as pd
import sqlite3

if not os.path.exists("veri"):
    os.mkdir('veri') #veri adında klasör oluşturduk
    archive = zipfile.ZipFile('pariteler_cikti_1hour_2022_2022.zip')
    archive.extractall("veri/") # parizeler zip dosyasınındaki verileri veri klasörünün içine attık
    tumdosyalar = os.listdir("veri")  # verideki tüm dosyaları listeledik
    pandas_csvlistesi = []
    for csv_dosya in tumdosyalar:
        veri = pd.read_csv("veri/" + csv_dosya)
        del veri["volume"]  # çıktıdan volume sütununu sildik.
        pandas_csvlistesi.append(veri)

    birlesmiscsv = pd.concat(pandas_csvlistesi)
    birlesmiscsv.to_csv('hepsi.csv', index=False)  # hepsini 1 csvde topladık. baştaki index numaraları olmadan

bag = sqlite3.connect("kripto.vt")
cursor = bag.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS parite("
               +"id INTEGER PRIMARY KEY AUTOINCREMENT,"
               +"otime DATETIME, open FLOAT,"
               +"high FLOAT, low FLOAT, close FLOAT);")
bag.commit()
bag.close()









