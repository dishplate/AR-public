# Get the keys in the api
~~~
response = requests.get(url="https://api.artic.edu/api/v1/artworks")
response.raise_for_status()
data = response.json()
#print(data["pagination"]["total"]).    #optional, peak into the data based on these keys
#print(data["pagination"]["current_page"])

for key, value in data.items():
    print(key)
~~~