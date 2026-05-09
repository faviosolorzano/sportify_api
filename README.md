# Favio Solorzano Cardenas 

# Sportify API

API REST para gestionar equipos deportivos y sus jugadores.

---

## Descripción

Esta API permite crear, editar, eliminar y buscar equipos de fútbol y sus jugadores.
Cada jugador pertenece a un equipo.

---

## Tecnologías usadas

- Python 3.14
- Django 6.0
- Django REST Framework 3.17
- SQLite

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio
2. Activar el entorno virtual: `venv\Scripts\activate`
3. Instalar dependencias: `pip install -r requirements.txt`
4. Aplicar migraciones: `python manage.py migrate`
5. Correr el servidor: `python manage.py runserver`

---

## Endpoints

### Equipos

| Método | URL | Descripción |
|--------|-----|-------------|
| GET | /api/teams/ | Listar equipos |
| POST | /api/teams/ | Crear equipo |
| PUT | /api/teams/{id}/ | Editar equipo |
| DELETE | /api/teams/{id}/ | Eliminar equipo |
| GET | /api/teams/?search= | Buscar equipo |

### Jugadores

| Método | URL | Descripción |
|--------|-----|-------------|
| GET | /api/players/ | Listar jugadores |
| POST | /api/players/ | Crear jugador |
| PUT | /api/players/{id}/ | Editar jugador |
| DELETE | /api/players/{id}/ | Eliminar jugador |

---

## Pruebas

Las pruebas se realizaron con Thunder Client (VS Code).

### Método: POST URL: http://127.0.0.1:8000/api/teams/

![](./Doc/post1.png)

### Método: GET URL: http://127.0.0.1:8000/api/teams/


![](./Doc/get.png)

### Método: PUT URL: http://127.0.0.1:8000/api/teams/1/

![](./Doc/put.png)

### Método: PATCH URL: http://127.0.0.1:8000/api/teams/1/

![](./Doc/patch.png)

### Método: GET URL: http://127.0.0.1:8000/api/teams/?search=Lima

![](./Doc/limaget.png)

### Método: GET URL: http://127.0.0.1:8000/api/teams/?search=segunda

![](./Doc/getsegunda.png)

### Método: DELETE URL: http://127.0.0.1:8000/api/teams/3/

![](./Doc/delete.png)

### Método: POST URL: http://127.0.0.1:8000/api/players/

![](./Doc/jugador2.png)

### Método: GET URL: http://127.0.0.1:8000/api/players/

![](./Doc/getjugador.png)

### Método: GET URL: http://127.0.0.1:8000/api/teams/1/

![](./Doc/totalj.png)

### Método: PUT URL: http://127.0.0.1:8000/api/players/1/

![](./Doc/putj.png)

### Método: GET URL: http://127.0.0.1:8000/api/players/?search=delantero

![](./Doc/getdelantero.png)

