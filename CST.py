import random
import math
import os
from datetime import date, timedelta

quotes = [ "Jangan mudah menyerah",
           "Hidup tak selalu mulus", 
           "Tidak ada yang peduli jika kau gagal",
           "Orang hanya peduli jika kau berhasil", 
           "Buatlah mereka iri dengan keberhasilanmu", 
           "Kegagalan bukanlah Akhir",  
           "Kerja Cerdas, Bukan Kerja Keras", 
           "High Risk, High Reward", 
           "Kejar sampai melebihi impianmu"
]

# SETUP PATH
folder_projek = os.path.dirname(os.path.abspath(__file__))
path_streak = os.path.join(folder_projek, "streak.txt")
path_durasi = os.path.join(folder_projek, "durasi.txt")
path_kemarin = os.path.join(folder_projek, "kemarin.txt")
path_tanggal = os.path.join(folder_projek, "tanggal.txt")

  # BACA Data
def ambil_data(path, default=0):
  if not os.path.exists(path): return default
  with open(path, "r") as file:
    isi = file.read().strip()
    return isi if default == "" else int(isi)

streakSekarang = ambil_data(path_streak)
totalMenit = ambil_data(path_durasi)
menitKemarin = ambil_data(path_kemarin)
tglTerakhir = ambil_data(path_tanggal, default="")
tglHariIni = date.today()

if tglTerakhir: 
  tglObjekTerakhir = date.fromisoformat(tglTerakhir)

  selisih = tglHariIni - tglObjekTerakhir
  if selisih > timedelta(days=1):
    print("Walah walah padam lur streakmu! Makane ojo bolos")
    streakSekarang = 0
    with open(path_streak, "w") as file: file.write("0")


quoteGenerator = random.choice(quotes)
print(f"Kata kata hari ini: {quoteGenerator}")

print(f"Streak belajar lo sekarang: {streakSekarang}, Sesi terakhir: {menitKemarin} menit")
jawaban = input("Hari ini coding nggak bro? (ya/tidak): ").lower()


if jawaban in ["ya","yoi","yes","yup"]:
  menitBaru = int(input("Hari ini belajar berapa menit bro?: "))
  
  if tglTerakhir == tglHariIni:
   print("⚠️ Streak Tidak Bertambah, Sudah Absen ⚠️")
  else:
   streakSekarang += 1
  with open(path_streak, "w") as file:
    file.write(str(streakSekarang))
  with open(path_tanggal, "w") as file:
    file.write(str(tglHariIni))
  print(f"Jojis tenan bro! streakmu masih {streakSekarang} hari!")

  totalMenit += menitBaru
  with open(path_durasi, "w") as file:
   file.write(str(totalMenit))
  with open(path_kemarin, "w") as file:
   file.write(str(menitBaru))

  print(f"Josjis meneh ancene arek iki! iseh sinau meneh ik. Total koding menitmu wes: {totalMenit/60:.1f} jam.")
else:
  print("Yawes istrahat sek, ojo dipekso boloo!") 

  
 



