import os,sys
G = '\033[1;32m'
P = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
logo=(f"""
{W}     oooo       .o.       ooooo        ooooo ooooo        
   `888      .888.      `888'        `888' `888'        
    888     .8"888.      888          888   888         
    888    .8' `888.     888          888   888         
    888   .88ooo8888.    888          888   888         
    888  .8'     `888.   888       o  888   888       o 
.o. 88P o88o     o8888o o888ooooood8 o888o o888ooooood8 
`Y888P    {GREEN}A {RED}L {WHITE}G                              
{W} ================================================
 [•] Admin      : Jalil XD
 [•] GitHub     : JALILHA
{W} ================================================
{W} [•]{G} NOTE{W}       :{G} REAL KEY TO FAKE KEY GENERATOR 
{W} ================================================""")
#####_____Def-Line_____#####
def line():
    print(f'{W} ================================================')
#####_____Def-Clear_____#####
def clear():
        os.system('clear')
        print(logo)
def home():
  clear()
  key=input(f"{W} [•]{G} Enter Fake Key {W}: ")
  line()
  k1,k2,k3,k4=key[:4],key[3:6],key[4:9],key[9:]
  intuid=int(key.split("#")[0])
  pref=str((intuid-104729)*2-37+(1-2**7))
  suff=str((intuid-523217)%104729)
  realid=(suff+k3+k1+k4+k2+pref).encode().hex()
  print(f"{W} [•]{G} Real Key :{W} {realid}")
  line()
  input(f"{W} [•]{G} Press Enter For Next Key ")
while True:
  home()
