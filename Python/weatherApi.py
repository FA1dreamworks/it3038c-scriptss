import json
import requests 

print('Please enter your zip code: ')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=45205,us&appid=840c2acf4796de91054cf355379acff2')
data=r.json()
print(data['weather'][0]['description'])

