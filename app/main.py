import json

from typing import Optional

from fastapi import FastAPI, status, Query

from models import Album


app = FastAPI()


@app.get(path='/')
def home():
    return {'Test API': 'Hello World!'}


@app.get('/api/json/')
def get_json():

    with open('data.json', 'r', encoding='utf-8') as f:

        results = json.loads(f.read())

        return results


@app.get('/api/json/albums')
def show_album(
        q: Optional[str] = Query(None)
):
    return q
