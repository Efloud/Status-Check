import requests
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored
import os 

responce_200 = []
responce_403 = []


def req(domain):
    try:
        url = requests.get(f"https://{domain}", timeout=0.5)
        if url.status_code == 200:
            responce_200.append(domain)
            print (colored("[200]", "green"), f"https://{domain}")

        elif url.status_code == 403:
            responce_403.append(domain) 
            print (colored("[403]", "red"), f"https://{domain}")
    except requests.exceptions.ConnectionError:
        pass


def main():

    domains_location = input("Domain Listesi Girin : ")
    liss = set()
    with open(domains_location, encoding="utf-8") as d:
        oku = d.read()
        parcala = oku.splitlines()
        for i in parcala:
            liss.add(i)
    with ThreadPoolExecutor(max_workers=200) as executor:
        executor.map(req, liss)



def cikti_kontrol(s_200, s_403, location=f"output.txt"):
    print("\n")
    s = input("Almak istediğiniz Çıktıyı giriniz => [200/403]: ")
    if s == "200":
        with open(location, "w", encoding="utf-8", encoding="utf-8") as s200:
            print(*s_200, file=s200, sep="\n")

    else:
        with open(location, "w", encoding="utf-8", encoding="utf-8") as s403:
            print(*s_403, file=s403, sep="\n")

    print(f"Kayıt Yeri : {os.getcwd()}\{location}")    

main()
cikti_kontrol(responce_200, responce_403)
