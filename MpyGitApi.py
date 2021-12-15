#Api para gestionatr y consultar los repositorios de github
#Autor: @mfluevano 
#Fecha: 2021-12-12

import requests
from fastapi import FastAPI

app = FastAPI()
#token github
token = 'temp'

#login github usign token
def login_github(token):
    url = 'https://api.github.com/user'
    headers = {'Authorization': 'token ' + token}
    response = requests.get(url, headers=headers)
    return response

@app.get("/v1")
def root():
    responseGit=login_github(token)
    return {"message": "Hellow Flat Digital", "github": responseGit.json()}


@app.get("v1/repos/{owner}/{repo}")
def get_repo(owner: str, repo: str):
    response = requests.get(f"https://api.github.com/repos/{owner}/{repo}")
    return response.json()

#Obtiene los commits de una repositorio
@app.post("v1/repos/{owner}/{repo}/commits")
def get_commits(owner: str, repo: str):
    response = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits")
    return response.json()

@app.post("v1/repos/{owner}/{repo}/authors")
def get_commits(owner: str, repo: str):
    response = requests.get(f"https://api.github.com/repos/{owner}/{repo}/authors")
    #Extrae los autores de los commits
    authors = []
    for author in response.json():
        authors.append(author['login'])
    #retorna los autores en formato json

    return authors.json()
    