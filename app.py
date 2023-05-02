import pandas as pd
import requests
import matplotlib.pyplot as plt
import json


#lastfm
api_key = '43ef4c5b06c364ab45ad9ac7a8b8080e'
username = 'loversssrock'

# Define o endpoint da API do Last.fm
url = 'http://ws.audioscrobbler.com/2.0/'

# Define os parâmetros da solicitação da API
params = {
    'method': 'user.gettopartists',
    'user': username,
    'api_key': api_key,
    'format': 'json',
    'limit': 10,
}

# Faz a solicitação da API e converte o resultado em um DataFrame do Pandas
response = requests.get(url, params=params)
data = response.json()


# Código para obter os dados do Last.fm
artists = pd.json_normalize(data['topartists']['artist'])[['name', 'playcount']]
artists = artists.astype({'playcount': int})  # Converte a coluna playcount para inteiro
artists = artists.sort_values(by='playcount', ascending=False)[:10]  # Ordena por playcount e seleciona os 10 artistas mais tocados
artists['index'] = range(len(artists))  # Adiciona uma coluna com os novos índices

print(artists)

# Código para plotar o gráfico

plt.bar(artists['index'], artists['playcount'])
plt.xticks(artists['index'], artists['name'], rotation=90)
plt.show()

