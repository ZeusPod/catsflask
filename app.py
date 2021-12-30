import json
import requests
import random
from flask import Flask, render_template
import requests

url = "https://api.thecatapi.com/v1/images/search?format=json&limit=50"

payload={}
headers = {
  'Content-Type': 'application/json',
  'x-api-key': '3dae19cc-78e0-45e1-b91b-91cce1f1ea56'
}

response = requests.request("GET", url, headers=headers, data = payload)
cats = response.json()

dicc = {}
for i in range(0,50):
    dicc[i] = cats[i]['url']

lista_urls = list(dicc.values())
print(lista_urls[0])

app = Flask(__name__) 

@app.route('/')
def home():
    return render_template('index.html', lista_urls=lista_urls[0])

#next photo
@app.route('/next')	
def next():
    return render_template('index.html', lista_urls=lista_urls[random.randint(0,49)])






