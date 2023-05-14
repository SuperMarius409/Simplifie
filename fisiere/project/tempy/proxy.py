import urllib3
import requests
import json

url = 'https://www.themealdb.com/api/json/v1/1/random.php'

try:
    meal = requests.get(url).json()
except:
    proxy = urllib3.ProxyManager('http://10.11.4.1:3128/')
    r1 = proxy.request('GET', url)
    meal = json.loads(r1.data.decode('utf-8'))

meals = meal["meals"]

# Loop through the meals and extract the ingredients
ingredients = []
for m in meals:
    for i in range(1, 21):
        ingredient = m[f'strIngredient{i}']
        if ingredient:
            ingredients.append(ingredient)

# Print the list of ingredients
print(ingredients)