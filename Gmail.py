#coding=utf-8
import smtplib,sys
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from os import system
from time import sleep
from getpass import getpass
from sys import version as versi_python
from datetime import datetime

sekarang = datetime.now()

hari = sekarang.day

bulan = sekarang.month

tahun = sekarang.year

jam = sekarang.hour

menit = sekarang.minute

detik = sekarang.second

#TEXT BERJALAN
def Aku(Dia):
	try:
		for kamu in Dia + '\n':
			sys.stdout.write(kamu)
			sys.stdout.flush()
			sleep(0.03)
	except NameError:
		exit("\033[1;92m[!] SEPERTINYA ANDA TELAH MENGUBAH ISI DARI CODE INI")

nama="""\033[1;94m****     **** *******     **     **\n/**/**   **/**/**////**   //**   ** \n/**//** ** /**/**   /**    //** **  \n/** //***  /**/*******      //***   \n/**  //*   /**/**///**       **/**  \n/**   /    /**/**  //**     ** //** \n/**        /**/**   //**   **   //**\n//         // //     //   //     // """

def tabel_waktu():
	print ("\033[1;91m╔═════════════════════════════════════╗\n║\033[1;91m[\033[1;93m•\033[1;91m] \033[1;92mAuthor : \033[1;93mMR-X JUNIOR             ║\n║\033[1;91m[\033[1;93m•\033[1;91m] \033[1;92mGitHub : \033[1;94mgithub.com/MR-X-Junior  ║\n║\033[1;91m[\033[1;93m•\033[1;91m] \033[1;92mWA.    : \033[1;95m+6285754629509          ║\n║\033[1;91m[\033[1;93m•\033[1;91m] \033[1;92mUPDATE : \033[1;96m16-12-2020 12:18.       ║")
	print ("\033[1;92m║\033[1;91m[\033[1;93m•\033[1;91m] \033[1;92mDATE   : \033[1;93m{}-\033[1;94m{}-\033[1;95m{} \033[1;96m{}:\033[1;96m{}:\033[1;96m{}     |\n|\033[91m[\033[93m•\033[91m] \033[92mVERSI  : \033[96m\033[92m1.0       \033[95m              |\n\033[1;97m╚═════════════════════════════════════╝".format(hari, bulan, tahun, jam, menit, detik))

if versi_python[0] in "2":
	exit('\033[93m[!] PROGRAM TIDAK DI DUKUNG PADA PYTHON VERSI 2')

try:
	#Rajin Ngoding :v
	user = []
	email = []
	password = []
	target = []
except IndexError:
	exit('\033[93m[!] INDEX ERROR')

def menu():
	system('clear')
	try:
		print(nama) ; tabel_waktu()
		Menu = input('\033[96mMENU UTAMA\n\033[92m====================\n\033[94m[\033[91m1\033[94m] \033[92mSPAM EMAIL\n\033[94m[\033[91m2\033[94m] \033[96mFROFIL AUTHOR\n\033[94m[\033[91m0\033[94m] \033[91mKELUAR\n\033[92m>>> \033[96m')
		if Menu == "":
			menu()
		elif Menu == "1" or Menu == "01":
			main()
		elif Menu == "2" or Menu == "02":
			author()
		elif Menu == "0" or Menu == "00":
			keluar()
		else:
			print ('\033[93m[!] KATA KUNCI DARI \033[95m"%s" \033[93mTIDAK DI TEMUKAN!...' % (Menu).upper()) ; sleep(3) ; menu()
	except NameError:
		exit('\033[93m[!] GAGAL MENJALANKAN PROGRAM')
	except KeyboardInterrupt:
		exit('\033[91m[!] KELUAR')

def keluar():
	system('clear')
	try:
		user.append(open('Name.txt','r').readline())
		exit ('\033[92m[✓] SELAMAT TINGGAL KAK \033[96m{}'.format(user[0].upper()))
	except FileNotFoundError:
		exit('\033[92m[✓] MAKASIH YA KAK UDAH PAKE SC NYA ^_^')
	except IndexError:
		exit('\033[93m[!] INDEX ERROR')

#FROFIL AUTHOR
def author():
	if tahun < 2006:
		exit('\033[91m[!] GW BELUM LAHIR GOBLOK')
	else:
		system('clear')
		try:
			print (nama)
			tabel_waktu()
			print ("\033[1;92mFROFIL AUTHOR")
			print ( 20* '\033[1;96m=')
			Aku ("\033[1;92mNAMA : \033[1;93mRAHMAT ADHA")
			if hari >= 13 and bulan >= 1 and tahun ==2021:
				Aku ("\033[1;92mUMUR : \033[1;94m15 TAHUN")
			if hari < 13 and bulan == 1 and tahun ==2021:
				Aku ("\033[1;92mUMUR : \033[1;94m14 TAHUN")
			if hari >= 13 and bulan >= 1 and tahun == 2022:
				Aku ("\033[1;92mUMUR : \033[1;94m16 TAHUN")
			if hari < 13 and bulan == 1 and tahun == 2022:
				Aku ("\033[1;92mUMUR : \033[1;94m15 TAHUN")
			if hari >= 13 and bulan >= 1 and tahun ==2023:
				Aku ("\033[1;92mUMUR : \033[1;94m17 TAHUN")
			if hari < 13 and bulan == 1 and tahun ==2023:
				Aku ("\033[1;92mUMUR : \033[1;94m16 TAHUN")
			if hari >= 13 and bulan >= 1 and tahun == 2024:
				Aku ("\033[1;92mUMUR : \033[1;94m18 TAHUN")
			if hari < 13 and bulan == 1 and tahun == 2024:
				Aku ("\033[1;92mUMUR : \033[1;94m17 TAHUN")
			if hari >= 13 and bulan >= 1 and tahun ==2025:
				Aku ("\033[1;92mUMUR : \033[1;94m19 TAHUN")
			if hari  < 13 and bulan == 1 and tahun ==2025:
				Aku ("\033[1;92mUMUR : \033[1;94m18 TAHUN")
			if hari >= 13 and bulan >= 1 and tahun == 2026:
				Aku ("\033[1;92mUMUR : \033[1;94m20 TAHUN")
			if hari < 13 and bulan == 1 and tahun == 2026:
				Aku ("\033[1;92mUMUR : \033[1;94m19 TAHUN")
			if hari >= 13 and bulan >= 1 and tahun >= 2027:
				Aku ("\033[92mUMUR : \033[94mLEBIH DARI 20 TAHUN ^_^")
			if hari  < 13 and bulan == 1 and tahun >= 2027:
				Aku ("\033[92mUMUR : \033[94m20 TAHUN")
			if tahun == 2020:
				Aku ("\033[1;92mUMUR : \033[1;94m14 TAHUN")
			Aku ("\033[1;92mLAHIR: \033[1;95m13 January, 2006\n\033[1;92mHOBI : \033[1;96mBELAJAR CODING ^_^\n\033[1;92mNO WA: \033[1;97m+62 85754629509")
			input ("\n\033[1;93m[ BACK ] ")
			menu()
		except NameError:
			exit("\033[1;92m[!] SEPERTINYA ANDA TELAH MENGUBAH ISI DARI CODE INI")
		except KeyboardInterrupt:
			exit("\033[1;93m[!] JANGAN MENEKAN TOMBOL CTRL + C\n[!] SELAMA PROGRAM MASIH BERJALAN")


def main():
	system('clear')
	try:
		email.append(open('Email.txt','r').readline())
		password.append(open('password.txt','r').readline())
		a = input (f'\033[92m[?] SPAM MENGGUNAKAN AKUN \033[95m{email[0]}\n\033[94m[\033[91m1\033[94m] \033[92mYES\n\033[94m[\033[91m2\033[94m] \033[93mNO\n\033[92m>>> \033[96m')
		if a == "No" or a == "no" or a == "2" or a == "02":
			no()
		elif a == "yes" or a == "Yes" or a == "1" or a == "01":
			yes()
		else:
			print ('\033[93m[!] PILIHAN TIDAK TERSEDIA')
			sleep(3)
			main()
	except KeyboardInterrupt:
		exit('\033[93m[!] KELUAR')
	except FileNotFoundError:
		system('clear')
		no()
									
def yes():
	system('clear')
	print (nama)
	tabel_waktu()
	print ('\033[92mPROSES SPAM') ; print (20* '\033[96m=')
	total = 0
	try:
			Target = input ('\033[92m[?] TARGET SPAM : \033[96m')
			if Target == "":
				print ('\033[93m[!] ISI DENGAN BENAR')
				sleep(3)
				main()
			subjek = input ('\033[92m[?] Subject : ')
			if subjek =="":
				print ('\033[93m[!] ISI DENGAN BENAR')
				sleep(3)
				main()
			pesan = input('\033[92m[?] ISI PESAN ANDA : ')
			if pesan == "":
			    	print ('\033[93m[!] ISI DENGAN BENAR')
			File = input('\033[92m[?] FILE UNTUK DI KIRIM : ')
			if File == "":
				print ('\033[93m[!] ISI DENGAN BENAR')
				sleep(3)
				main()
			path = input ('\033[92m[?] PATH KE : ')
			if File == "":
				print ('[!] ISI DENGAN BENAR')
				sleep(3)
				main()
			else:
				target.append(Target)
				print ('\033[93m[!] MOHON TUNGGU')
				while True:
					fromaddr = email[0]
					toaddr = target[0]
					 
					msg = MIMEMultipart()
					 
					msg['From'] = fromaddr
					msg['To'] = toaddr
					msg['Subject'] = subjek
					 
					body = pesan 
					 
					msg.attach(MIMEText(body, 'plain'))
					
					filename = File
					attachment = open(path, "rb")
					 
					
					part = MIMEBase('application', 'octet-stream')
					part.set_payload((attachment).read())
					encoders.encode_base64(part)
					part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
					 
					msg.attach(part)
					 
					server = smtplib.SMTP('smtp.gmail.com', 587)
					server.starttls()
					server.login(fromaddr, password[0])
					text = msg.as_string()
					server.sendmail(fromaddr, toaddr, text)
					server.quit()
					print ('\033[92m[✓] BERHASIL')
					total += 1
	except smtplib.SMTPServerDisconnected:
		exit('\033[93m[!] SAMBUNGAN TERPUTUS')
	except TimeoutError:
		exit('\033[93m[!] GAGAL TERHUBUNG KE SERVER')
	except smtplib.SMTPAuthenticationError:
		print ('\033[93m[!] USERNAME : \033[92m{}'.format(email[0]))
		print ('\033[93m[!] PASSWORD : \033[95m{}'.format(password[0]))
		system ('rm email.txt') ; system('rm password.txt')
		exit('\033[91m[!] GAGAL LOGIN KE AKUN')
	except socket.gaierror:
		exit('\033[91m[!] TIDAK ADA KONEKSI')
	except smtplib.SMTPRecipientsRefused:
		exit('\033[93m[!] PENGGUNA TIDAK DI TEMUKAN')
	except IsADirectoryError:
		exit('\033[93m[!] TERJADI KESALAHAN YANG TIDAK DI KETAHUI')
	except PermissionError:
		exit('\033[91m[!] GAGAL MENGAKSES PENYIMPANAN')
	except FileNotFoundError:
		print (f'\033[93m[!] FILE \033[96m"{File}" \033[93mTIDAK DI TEMUKAN')
	except KeyboardInterrupt:
		print ('\n\033[92m[✓] TOTAL SPAM : \033[96m',total)
		back = input ('\033[93m[?] BACK [Y/N]')
		if back == "Y" or back == "y":
			menu()
		elif back == "n" or back == "N":
			exit('\033[94m[\033[91m1\033[94m] \033[91mKeluar')
		else:
			exit('\033[93m[!] PILIHAN TIDAK TERSEDIA')
		
def no():
	total = 0
	system('clear')
	print (nama)
	tabel_waktu()
	print ('\033[92mPROSES SPAM') ; print (20* '\033[96m=')
	try:
		pengirim = input ('\033[92m[?] EMAIL PENGIRIM : \033[96m')
		if pengirim == "":
			print ('\033[93m[!] MOHON ISI DENGAN BENAR')
			sleep(3)
			no()
		with open ('email.txt','w') as a:
			a.write(pengirim) ; a.close()
		password = getpass ('\033[92m[?] PASSWORD AKUN GOOGLE : \033[93m')
		if password == "":
			print ('\033[91m[!] ISI DENGAN BENAR')
			sleep(3)
			no()
		with open ('password.txt','w') as b:
			b.write(password) ; b.close()
		penerima = input ('\033[91m[?] TARGET : \033[93m')
		if penerima == "":
			print ('\033[91m[!] ISI DENGAN BENAR')
			sleep(3)
			no()
		subjek = input ('\033[92m[?] SUBJEK : \033[93m')
		if subjek == "":
			print ('\033[91m[!] ISI DENGAN BENAR')
			sleep(3)
			no()
		pesan = input ('\033[92m[?] PESAN ANDA : \033[93m')
		if pesan == "":
			print ('\033[93m[!] ISI DENGAN BENAR')
			sleep(3)
			no()
		File = input ('\033[92m[?] FILE UNTUK DI KIRIM : \033[93m')
		if File == "":
			print ('\033[91m[!] ISI DENGAN BENAR')
			sleep(3)
			no()
		path = input ('\033[92m[?] PATH KE : \033[95m')
		if path == "":
			print ('\033[91m[!] ISI DENGAN BENAR')
			sleep(3)
			no()
		else:
			target.append(penerima)
			print ('\033[93m[!] MOHON TUNGGU')
			while True:
				fromaddr = pengirim
				toaddr = penerima
				 
				msg = MIMEMultipart()
				 
				msg['From'] = fromaddr
				msg['To'] = toaddr
				msg['Subject'] = subjek
				 
				body = pesan 
				 
				msg.attach(MIMEText(body, 'plain'))
				
				filename = File
				attachment = open(path, "rb")
				 
				
				part = MIMEBase('application', 'octet-stream')
				part.set_payload((attachment).read())
				encoders.encode_base64(part)
				part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
				 
				msg.attach(part)
				 
				server = smtplib.SMTP('smtp.gmail.com', 587)
				server.starttls()
				server.login(fromaddr, password)
				text = msg.as_string()
				server.sendmail(fromaddr, toaddr, text)
				server.quit()
				print ('\033[92m[✓] BERHASIL')
				total += 1
	except smtplib.SMTPServerDisconnected:
		exit('\033[93m[!] SAMBUNGAN TERPUTUS')
	except TimeoutError:
		exit('\033[93m[!] GAGAL TERHUBUNG KE SERVER')
	except smtplib.SMTPAuthenticationError:
		print ('\033[93m[!] USERNAME : \033[92m{}'.format(pengirim))
		print ('\033[93m[!] PASSWORD : \033[95m{}'.format(password))
		system ('rm email.txt') ; system('rm password.txt')
		exit('\033[91m[!] GAGAL LOGIN KE AKUN ')
	except socket.gaierror:
		exit('\033[91m[!] TIDAK ADA KONEKSI')
	except smtplib.SMTPRecipientsRefused:
		exit('\033[93m[!] PENGGUNA TIDAK DI TEMUKAN')
	except IsADirectoryError:
		exit('\033[93m[!] TERJADI KESALAHAN YANG TIDAK DI KETAHUI')
	except PermissionError:
		exit('\033[91m[!] GAGAL MENGAKSES PENYIMPANAN')
	except FileNotFoundError:
		print (f'\033[93m[!] FILE \033[96m"{File}" \033[93mTIDAK DI TEMUKAN')
	except KeyboardInterrupt:
		print ('\033[92m[✓] TOTAL SPAM : \033[93m',total)
		kembali = input('\033[93m[!] BACK \033[94m[\033[92mY/\033[97mN\033[94m]')
		if kembali == "":
			exit('\033[93m[!] PILIHAN TIDAK TERSEDIA')
		elif kembali == "Y" or kembali == "y":
			menu()
		elif kembali == "n" or kembali == "N":
			exit('\033[94m[\033[91m!\033[94m] \033[91mKeluar')
		else:
			exit('\033[93m[!] PILIHAN TIDAK TERSEDIA')
			
		
if __name__=="__main__":
	menu()