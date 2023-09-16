import requests

def search():
    user = input('Target Username: ')
    
    sites = ["facebook", "instagram", "twitter", "giphy"]
    u_sites = ["9gag", "reddit"]
    tiktok = ["tiktok"]

    for site in sites:
        url = f"https://www.{site}.com/{user}"
        output = requests.get(url)    

        if output.status_code == 200:
            print(f"[-] {site}: {url}")

    for site in tiktok:
        url = f"https://www.{site}.com/@{user}"
        output = requests.get(url)    

        if output.status_code == 200:
            print(f"[-] tiktok: {url}")

    for site in u_sites:
        url = f"https://www.{site}.com/u/{user}"
        output = requests.get(url)

        if output.status_code == 200:
            print(f"[-] {site}: {url}")
