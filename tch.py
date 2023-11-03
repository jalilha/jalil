import os;import sys;import time;import codecs

cout = 0

Green  ="\x1b[1;92m"
RED  ='\x1b[1;91m'
logo = '''\033[2;36m
  _                     _         _        __      _____  
 | |                   | |       | |       \ \    / /__ \ 
 | |     __ _ _ __ ___ | |__   __| | __ _   \ \  / /   ) |
 | |    / _` | '_ ` _ \| '_ \ / _` |/ _` |   \ \/ /   / / 
 | |___| (_| | | | | | | |_) | (_| | (_| |    \  /   / /_ 
 |______\__,_|_| |_| |_|_.__/ \__,_|\__,_|     \/   |____|
                                                          
                                                          
'''


os.system('clear')
print(logo)
file = input(Green+' اسم الملف > ')
cot = int(input('\033[91m  عدد التشفير > '))
if cot < 100000000:
                out = file.replace('.py', '') + '-enc.py'
                file = open(file).read()
                dn = codecs.encode(file, 'rot_13')
                
                a = repr(dn)
                
                
                s = open(out, 'w')
                s.write("#https://t.me/j_b_i\nexec((lambda __, _, : _(''" + str(a) + "'',__))('rot_13',__import__('codecs').decode))")
                s.close()
                while True:
                    if cot >= cout:
                        filez = open(out).read()
                        dn2 = codecs.encode(file, 'rot_13')
                        
                      
                        ab = repr(dn2)
                        
                        
                        X = open(out, 'w')
                        X.write("#https://t.me/j_b_i\nexec((lambda __, _, : _(''" + str(ab) + "'',__))('rot_13',__import__('codecs').decode))")
                        X.close()
                        cout += 1
                        continue
                    break
                print ('\x1b[1;94m[\x1b[1;92m\x1b[1;94m] \x1b[1;97 File saved as \x1b[1;96m{ \x1b[1;92m%s \x1b[1;96m}' % out)
