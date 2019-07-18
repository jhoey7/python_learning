import requests
r = requests.get("https://www.fontsquirrel.com/fonts/source-code-pro")
print(r.status_code)
print(r.ok)