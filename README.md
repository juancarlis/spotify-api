# Spotify API Challenge

## Challenge
Utilizando la API de Spotify crear un endpoint al que ingresando el nombre de la banda se obtenga un array de toda la discografía en el siguiente formato:

```json
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
```

El endpoint de consulta debe ser el siguiente:
<**http://localhost/api/v1/albums?q=<band-name>**>

- Se puede usar un microframework (como FastAPI)
- Se pueden usar librerías (como requests)
- No se puede usar ningún SDK de Spotify

## Desarrollo
Este proyecto puede ser ejecutado localmente desde la terminal, desde Poetry o desde Docker


### Prerequisitos

##### FastAPI[https://fastapi.tiangolo.com/]
```
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
```
