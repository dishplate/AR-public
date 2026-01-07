#file to test api's
import requests

baseurl = "https://rickandmortyapi.com/api/"
endpoint = "character"
r = requests.get(baseurl + endpoint)
data = r.json()
# print(data)
# print(data['info']['pages']) #this works
info = data['info']
pages = info['pages']
next = info['next']
print(f'next url= {next} and \n pages={pages}')
page_count = []
while page_count < 43:
    print('hello')
    page_count.append=+1
    break