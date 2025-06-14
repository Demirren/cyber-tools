# main.py

import requests

ip = input("Enter IP: ")
url = f"https://api.hackertarget.com/reverseiplookup/?q={ip}"

try:
    res = requests.get(url)
    if res.status_code == 200:
        print("\nReverse IP Lookup Results:\n")
        print(res.text)
    else:
        print(f"Error: Received status code {res.status_code}")
except Exception as e:
    print(f"Request failed: {e}")
