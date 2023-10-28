try:
    prox= requests.get('https://raw.githubusercontent.com/trt-Fire/data/main/proxies.txt').text
    open('proxies.txt','w').write(proxies)
except Exception as e:
    print('\x1b[1;92m[√] PLEASE WAIT CHECKING USMAN GULL UPDATE...')
	
proxies=open('proxies.txt','r').read().splitlines()


android_models=[]
try:
    xx = requests.get('https://raw.githubusercontent.com/trt-Fire/data/main/strings.txt').text.splitlines()
    for line in xx:
        android_models.append(line)
except:pass

usr=[]
try:
    xd=requests.get('https://raw.githubusercontent.com/trt-Fire/data/main/ua.txt').text.splitlines()
    for us in xd:
        usr.append(us)
