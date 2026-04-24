import random
import math
import os
from datetime import date

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

tglHariIni = str(date.today())


quotes = [ "Jangan mudah menyerah",
           "Hidup tak selalu mulus", 
           "Tidak ada yang peduli jika kau gagal",
           "Orang hanya peduli jika kau berhasil", 
           "Buatlah mereka panas dengan keberhasilanmu", 
           "Kegagalan bukanlah Akhir",  
           "Tidak ada resiko tidak ada uang", 
           "No Risk No Bitches", 
           "Kejar sampai melebihi impianmu"
]

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
    file.write(tglHariIni)
  print(f"Jojis tenan bro! streakmu masih {streakSekarang} hari!")

  totalMenit += menitBaru
  with open(path_durasi, "w") as file:
   file.write(str(totalMenit))
  with open(path_kemarin, "w") as file:
   file.write(str(menitBaru))

  print(f"Josjis meneh ancene arek iki! iseh sinau meneh ik. Total koding menitmu wes: {totalMenit/60:.1f} jam.")
else:
  print("Yawes istrahat sek, ojo dipekso boloo!") 

  
 



