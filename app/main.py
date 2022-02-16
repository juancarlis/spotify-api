""" API Docs


"""
# Python
import json

# Fastapi
from typing import Optional
from fastapi import FastAPI, status, Query

# Project modules
from backend import Spotiapi
from config.common import config


app = FastAPI()
api = Spotiapi(config()['CLIENT_ID'], config()['CLIENT_SECRET'])

api.authorize()


@app.get(path='/')
def home():
    return 'SpotiAPI for Banza Challenge'


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
        - json in the format:

        [{	
            "name": "Album Name",
            "released": "10-10-2010",
            "tracks": 10,
            "cover":{
                    "height": 640, 
                    "width": 640,
                    "url": "https://i.scdn.co/image/6c951f3f334e05ffa"
                    }
        },
        {
            ...
        }]

    """

    return api.get_albums(q)
