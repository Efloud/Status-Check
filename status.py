import requests
from concurrent.futures import ThreadPoolExecutor
save_domain_list = []


def req(domain):
    try:
        url = requests.get(f"https://{domain}", timeout=0.5)
        if url.status_code == 200:
            save_domain_list.append(domain)
            print("[200] ", domain)
        if url.status_code == 403:
            save_domain_list.append(domain) 
            print("[403] ", domain)
    except requests.exceptions.ConnectionError:
        pass


def main():
    domains_location = input("Domain Listesi Girin : ")
    liss = []
    with open(domains_location, encoding="utf-8") as d:
        oku = d.read()
        split = oku.splitlines()
        for i in split:
            liss.append(i)
    with ThreadPoolExecutor(max_workers=200) as executor:
        executor.map(req, liss)


def save_to_file(content, save_location=r"output.txt"):
    with open(save_location, 'w') as files:
        print(*content , file=files, sep="\n")


main()
save_to_file(save_domain_list)
