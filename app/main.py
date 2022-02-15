""" API Docs


"""


import json

from typing import Optional

from fastapi import FastAPI, status, Query

# from models import Album
from backend import Spotiapi
from config.common import config


app = FastAPI()
api = Spotiapi(config()['CLIENT_ID'], config()['CLIENT_SECRET'])

api.authorize()


@app.get(path='/')
def home():
    return {'Test API': 'Hello World!'}


@app.get(
    path='/api/v1/albums',
    status_code=status.HTTP_200_OK,
    summary='Search all the albums from a band.',
    tags=['Albums']
)
async def search_albums(q: Optional[str] = Query(None)):
    """Search information of all the albums of a chosen band.

    Parameters:
        - q: Query format of the name of the band to search for.

    Returns: 
        - 
    """
    print(api.headers)

    return api.get_albums(q)
