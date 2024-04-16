
import json
import requests


ICO = input("Zadejte IČO subjektu, o kterém chcete získat informace:")
response = requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ICO}")

if response.text and response.status_code == 200:
    data = response.json()


obchodniJmeno = data.get('obchodniJmeno')
textovaAdresa = data.get("sidlo").get('textovaAdresa')

print( f"{obchodniJmeno}, {textovaAdresa}")


#2

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

nazev_subjektu = input("Název subjektu, který chcete vyhledat: ")

data ={"obchodniJmeno": nazev_subjektu}
res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, json=data)
subjekty = res.json()

pocet_celkem = subjekty["pocetCelkem"]
print(f"Nalezeno {pocet_celkem} subjektů:\n")


ekonomicke_subjekty = subjekty["ekonomickeSubjekty"]
for subjekt in ekonomicke_subjekty:

    print(f"{subjekt['obchodniJmeno']}, {subjekt['ico']}")
