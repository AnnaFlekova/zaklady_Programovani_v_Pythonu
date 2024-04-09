
import json
import requests

input ("Zadejte IČO subjektu, o kterém chcete získat informace:")
ICO = input
response = requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ICO}")

if response.text and response.status_code == 200:
    data = response.json()


obchodniJmeno = data.get('obchodniJmeno')
textovaAdresa = data.get('textovaAdresa')

print( f"{obchodniJmeno}, {textovaAdresa}")


#2

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

input("Název subjektu, který chcete vyhledat: ")
nazev_subjektu = input

data ={"obchodniJmeno": nazev_subjektu}
res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)
subjekty = res.json()
pocet_subjektu = len(subjekty)

print(f"Nalezeno {pocet_subjektu} subjektů:\n")

for subjekt in subjekty:
    
    print(f"{subjekt['obchodniJmeno']}, {subjekt['ico']}")