import requests
import json
from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

@app.get("/api/hello")
def hello_world():
    '''
    Função de exemplo para retornar uma mensagem simples.'''
    return {"message": "Hello, World!"} 

@app.get("/api/restaurantes/")
def lista_restaurantes(restaurante: str = Query(None)):
    '''
    Função para retornar informações de restaurantes.
    Se um restaurante específico for solicitado, retorna informações sobre ele.
    Caso contrário, retorna informações de todos os restaurantes.
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    if response.status_code == 200:
        dados_json = response.json()
        if restaurante == None:
            print (f'Retornando todos os restaurantes')
            return {'Dados': dados_json} 
        else:
            print (f'Buscando informações do restaurante: {restaurante}')
        
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
                })

        return {'restaurante': restaurante, 'Cardapio':dados_restaurante}
    else:
        print ('Erro',f'{response.status_code} - {response.text}')