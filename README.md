# Spotify API Challenge

## Challenge
Utilizando la API de Spotify crear un endpoint al que ingresando el nombre de la banda se obtenga un array de toda la discografía en el siguiente formato:

```json
[{	"name": "Album Name",
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

##### [FastAPI](https://fastapi.tiangolo.com/)
```
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
```
	
##### [Pandas](https://pandas.pydata.org/docs/)
```
Pandas is a Python package that provides fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python. Additionally, it has the broader goal of becoming the most powerful and flexible open source data analysis / manipulation tool available in any language. It is already well on its way towards this goal.
```
	
##### [Poetry](https://python-poetry.org/)
```
Poetry helps you declare, manage and install dependencies of Python projects, ensuring you have the right stack everywhere.
```
	
##### [Docker](https://docs.docker.com/get-started/overview/)
```
Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications. By taking advantage of Docker’s methodologies for shipping, testing, and deploying code quickly, you can significantly reduce the delay between writing code and running it in production.
```
	
##### [Docker Compose](https://docs.docker.com/compose/)
```
Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.
```

## Deploy del servidor (Local)
Existen diversas formas de correr el proyecto. Se debe montar necesariamente sobre un SO basado en Linux. En caso de querer ejecutarlo en un entorno Windows se recomienda activar el [WSL](https://docs.microsoft.com/en-us/windows/wsl/install) e instalar una distribución de Linux. 
	
### Poetry
En caso de tener instalado Poetry en el equipo, el servidor se lanza desde la carpeta app dentro del proyecto:
```bash
poetry run uvicorn main:app --host 0.0.0.0 --port 8000
```
Y para que recargue en caso de detectar cambios:
```bash
poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
	
### Docker
Mi método favorito.
Primero buildeamos los servicios:
```bash
docker-compose build
```
Luego corremos con:
```bash
docker-compose up
```
	
### Python puro
En caso de no contar con Docker o Poetry se deja un archivo requirements.txt para lanzar el proyecto con Python puro.
	
Primero se crea un entorno virtual y se lo activa:
```bash
python3 -m venv venv
source venv/bin/activate
```
Luego, se instalan las dependencias del proyecto:
```bash
pip install -r requirements.txt
```
	
Finalmente se levanta el servidor con Uvicorn desde la carpeta app dentro del proyecto.
```bash
cd app
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
## Test API
Una vez lanzado el servidor verificar en un navegador ir a:
 - http://localhost:80/ si se utilizó Docker
 - http://localhost:8000/ si se utilizó método distinto de Docker

Luego puede testear el endpoint:
	
/api/v1/albums?q=Band+Name
	
Por ejemplo:
http://localhost/api/v1/albums?q=Iron+Maiden

