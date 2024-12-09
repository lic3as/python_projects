import requests
url = "https://www.youtube.com"

try:
    if requests.get(url).status_code == 200:
        print("\33[1;32mO servidor está disponível.\033[m")
except:
    print("\033[0;31mO servidor não está disponível.\033[m")
