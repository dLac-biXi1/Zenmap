import os
import colorama
from colorama import Fore, Style


#Burada kali Linux'e Yüklenecek Dosyalar Var 
os.system("apt-get update")
os.system("apt-get intsall figlet")
os.system("apt-get install nmap")
os.system("clear")
os.system("figlet ZeNmap")



#Ekranda Çıkacak İşlemler
print(Fore.YELLOW + """
1 = Ping Scan

2 = Quick Scan 

3 = Quick Plus Scan

4 = Quick traceroute

5 = Intence Scan 

6 = Intence Plus UDP Scan 

7 = Intence Scan and All TCP Ports

8 = Instense Scan and No Ping

9 = Regular Scan

10 = Slow Comprehensive Scan

12 = Yardım

		İnstagram = https://www.instagram.com/iskender_eren_goktas
		YouTube = https://www.youtube.com/channel/UCgC7g7CU5E4taGVpEcR9z4A
""")
#İşlem numarası == no
no = int(input("İşlem Numarası Giriniz :----> "))


if no == 1:
	ıp = input("IP Adresi Giriniz :----> ")
	print(" ")
	print('\033[1m' + "Çalıştırılan Komut = nmap -sn ")
	print(" ")
	print(" ")
	os.system("nmap -sn " + ıp)
	print(" ")
	print("Başarılı Bir Şekilde Tarandı.")
	print(" ")

elif no == 2:
	ıp1 = input("IP Adresi Giriniz :----> ")
	print(" ")
	print('\033[1m' + "Çalıştırılan Komut = nmap -T4 -F")
	print(" ")
	print(" ")
	os.system("nmap -T4 -F " + ıp1)
	print(" ")
	print("Başarılı Bir Şekilde Tarandı.")
	print(" ")
	

elif no == 3:
	print(" ")
	ıp2 = input("IP Adresi Giriniz : ")
	print('\033[1m' + "Çalıştırılan Komut = nmap -sV -T4 -O -F --version-light ")
	print(" ")
	print(" ")
	os.system("nmap -sV -T4 -O -F --version-light " + ıp2)
	print(" ")
	print("Başarılı Bir Şekilde Tarandı.")
	print(" ")
	

elif no == 4:
	print(" ")
	ıp3 = input("IP Adresi Giriniz : ")
	print('\033[1m' + "Çalıştırılan Komut = nmap -sn --traceroute")
	print(" ")
	print(" ")
	os.system("nmap -sn --traceroute " + ıp3)
	print(" ")
	print("Başarılı Bir Şekilde Tarandı.")
	print(" ")
	

elif no == 5:
	print(" ")
	ıp4 = input("IP Adresi Giriniz : ")
	print('\033[1m' + "Çalıştırılan Komut = nmap -T4 -A -A -v")
	print(" ")
	print(" ")
	os.system("nmap -T4 -A -v " + ıp4)
	print(" ")
	print("Başarılı Bir Şekilde Tarandı.")
	print(" ")
	

elif no == 6:
	print(" ")
	ıp5 = input("IP Adresi Giriniz :----> ")
	print('\033[1m' + "Çalıştırılan Komut = nmap -sS -sU -T4 -A -v")
	print(" ")
	print(" ")
	os.system("nmap -sS -sU -T4 -A -v " + ıp5)
	print(" ")
	print("Başarılı Bir Şekilde Tarandı.")
	print(" ")

elif no == 7:
	print(" ")
	ıp6 = input("IP Adresi Giriniz :----> ")
	print('\033[1m' + "Çalıştırılan Komut = nmap -p 1-65535 -T4 -A -v")
	print(" ")
	print(" ")
	os.system("nmap -p 1-65535 -T4 -A -v " + ıp6)
	print(" ")
	print("Başarılı Bir Şekilde Tarandı.")
	print(" ")
	

elif no == 8:
	print("")
	ıp7 = input("IP Adresi Giriniz :----> ")
	print('\033[1m' + "Çalışan Komut = nmap -T4 -A -v -Pn")
	print(" ")
	print(" ")
	os.system("nmap -T4 -A -v -Pn " + ıp7)
	print(" ")
	print("Başarılı Bir Şekilde Tarandı.")
	print(" ")
	
	

elif no == 9:
	print("")
	ıp8 = input("IP Adresi Giriniz :----> ")
	print('\033[1m' + "Çalıştırılan Komut = nmap")
	print(" ")
	print(" ")
	os.system("nmap " + ıp8)
	print(" ")
	print("Başarılı Bir Şekilde Tarandı.")
	print(" ")
	

elif no == 10:
	ıp9 = input("IP Adresi Giriniz :----> ")
	print("")
	print('\033[1m' + "Çalıştırılan Komut = nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script ""default or (discovery and safe) ")
	print(" ")
	print(" ")
	os.system("nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script ""default or (discovery and safe)""" + ıp9 )
	print(" ")
	print("Başarılı Bir Şekilde Tarandı.")
	print(" ")

elif no == 11:
	print("""
1 = ZenMap Nedir?

2 = ZeNmap Ne İşe Yarar?
""")
	yardım = int(input("Yardım Numarası Giriniz :----> "))
	if yardım == 1:
		print("		ZeNmap bir Nmap Araçıdır. ")
	elif yardım == 2:
		print("		ZeNmap Nmap'ın çok kullanışlı olan komutlarını kolayca çalıştırmamıza olanak sağlayan bir araçtır.")
	else:
		print(Fore.BLUE + '\033[1m' + "                  !!! Hatalı Tuşlama Yaptınız Program kapatıldı !!!")
		os.system("exit")
else:	
	print(Fore.BLUE + '\033[1m' + "                  !!! Hatalı Tuşlama Yaptınız Program kapatıldı !!!")
	os.system("exit")


tekrar = input("Tekrar Başlatmak İstermisiniz (Y/N) :----> ")

if tekrar == "Y":
	os.system("python3 zenmap.py")
else:
	print("      -------- !!! Program Kapatıldı !!! --------")




