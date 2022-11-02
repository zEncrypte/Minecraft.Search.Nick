import os    
import requests
from pystyle import *

System.Clear()
System.Title("Minecraft Search Nick")
Cursor.HideCursor()

p = Colors.purple
w = Colors.white
y = Colors.yellow
r = Colors.red
c = Colors.cyan
lr = Colors.light_red
lb = Colors.light_blue
lg = Colors.light_green

trip = Colors.StaticMIX((p, w, r))
trip2 = Colors.StaticMIX((c, w, w))
dual1 = Colors.StaticMIX((c, w))
dual2 = Colors.StaticMIX((lb, w))

def dangerous(ZeroTwo: str, nagatoro: str = '...') -> str:
    if nagatoro == '...':
      return print(f""" {Col.Symbol(nagatoro, lb, p)} {lb}{ZeroTwo}{Col.reset}""")
    else:
      return f""" {Col.Symbol(nagatoro, y, p)} {p}{ZeroTwo}{Col.reset}"""

while True:
    ban = """
 ██████   ██████  █████████  ██████   █████
░░██████ ██████  ███░░░░░███░░██████ ░░███ 
 ░███░█████░███ ░███    ░░░  ░███░███ ░███ 
 ░███░░███ ░███ ░░█████████  ░███░░███░███ 
 ░███ ░░░  ░███  ░░░░░░░░███ ░███ ░░██████ 
 ░███      ░███  ███    ░███ ░███  ░░█████ 
 █████     █████░░█████████  █████  ░░█████
░░░░░     ░░░░░  ░░░░░░░░░  ░░░░░    ░░░░░ 
                                            """[1:]



    ban = Colorate.Vertical(Colors.DynamicMIX((trip, dual1)), Center.XCenter(ban))
    print(ban)
    nsn = input(dangerous(f"Introduce el Nick {lr}-> ", '*')).replace('"','').replace("'","")
    req = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{nsn}")
    sts = req.status_code
    if sts == 200:
        print(f" {p}[{r}!{p}] {dual2}Este usuario es premium :(\n")
        input(f" {p}[{y}*{p}] {lr}Presiona enter para continuar...")
        os.system("cls")
    elif sts == 204:
        print(f" {p}[{lg}+{p}] {trip2}Usuario disponible :)\n")
        input(f" {p}[{y}*{p}] {lr}Presiona enter para continuar...")
        os.system("cls")
