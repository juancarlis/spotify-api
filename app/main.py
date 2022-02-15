import json

from typing import Optional

from fastapi import FastAPI, status, Query

from models import Album
from backend import Spotiapi
from config.common import config


app = FastAPI()
api = Spotiapi(config()['CLIENT_ID'], config()['CLIENT_SECRET'])


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


@app.get(
    path='/api/v1/albums',
    response_model=Album,
    status_code=status.HTTP_200_ok,
    summary='Search all the albums from a band.',
    tags=['Albums']
)
async def search_albums():
    pass
