import requests, os, pyfiglet
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored

banner = pyfiglet.figlet_format("EfStatusCheck")
responce_200 = []
responce_403 = []
toplam = 0


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

    print(colored(banner, "red"), end="")
    print("-"*40, sep="")
    domains_location = input("Domain Listesi Girin : ")
    print("-"*40, "\n", sep="", end="")
    
    liss = set()
    global toplam
    with open(domains_location, encoding="utf-8") as d:
        oku = d.read().splitlines()
        for i in oku:
            liss.add(i)
            toplam += 1

    with ThreadPoolExecutor(max_workers=200) as executor:
        executor.map(req, liss)
        
    print("-"*40)
    print("Toplam Taranan Sayısı: ", colored(f"[{toplam}]", "red"), sep="")


def cikti_kontrol(s_200, s_403, location=f"output.txt"):
    
    sorgu = input("Almak istediğiniz => [200/403]: ")
    if sorgu == "200":
        with open(location, "w", encoding="utf-8") as s200:
            print(*s_200, file=s200, sep="\n")
            print(f"Kayıt Yeri : {os.getcwd()}", "\n", "-"*40 , sep="")  
            
    elif sorgu == "403":
        with open(location, "w", encoding="utf-8") as s403:
            print(*s_403, file=s403, sep="\n")
            print(f"Kayıt Yeri : {os.getcwd()}", "\n", "-"*40 , sep="")  
    
    else:
        print("Lütfen 200 veya 400 Çıktısını Almayı DENEYİN!", "\n", "-"*40, sep="")

    
main()
cikti_kontrol(responce_200, responce_403)
quit()
