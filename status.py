import requests
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored

responce_200 = []
responce_403 = []


def req(domain):

    try:
        url = requests.get(f"https://{domain}", timeout=0.5)
        if url.status_code == 200:
            responce_200.append(domain)
            print (colored("[200]", "green"), f"https://{domain}")

        if url.status_code == 403:
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


def save_200(content, save_location="200.txt"):
    yaz = open(save_location, 'w')
    print(*content , file=yaz, sep="\n")


def save_403(content, save_location="403.txt"):
    yaz = open(save_location, 'w')
    print(*content , file=yaz, sep="\n")


main()
save_200(responce_200)
save_403(responce_403)
