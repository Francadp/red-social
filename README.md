# Red social minimalista con FastAPI

Trabajo final de Práctica Profesionalizante I (ITSC). API REST con usuarios, posts, likes, follows y feed, con autenticación JWT.

## Estructura

```
.
├── app/
│   ├── main.py          # crea la app y conecta los routers
│   ├── database.py      # engine y sesión
│   ├── models.py        # tablas y schemas
│   ├── security.py      # hash de contraseñas y tokens jwt
│   ├── dependencies.py  # sesión, usuario actual y permisos
│   ├── routers/         # auth, users, posts y feed
│   └── tests/           # tests con pytest
├── pyproject.toml
└── uv.lock
```

## Instalación

Hace falta tener [uv](https://docs.astral.sh/uv/) instalado.

```bash
git clone https://github.com/Francadp/red-social.git
cd red-social
uv sync
```

## Correr la API

Desde la carpeta raíz del repositorio:

```bash
uv run fastapi dev app/main.py
```

La documentación queda en http://127.0.0.1:8000/docs. Para los endpoints protegidos hay que registrarse en `/auth/register` y después usar el botón Authorize.

## Tests

Los tests se corren desde la carpeta `app`, porque ahí está el `pytest.ini`:

```bash
cd app
uv run pytest -q
```

## Ramas

| Rama | Qué agrega |
|---|---|
| `feat/auth` | registro, login con JWT y usuario actual |
| `feat/auth-in-crud` | posts protegidos: el autor sale del token y solo el autor edita o borra |
| `feat/like` | likes y cantidad de likes por post |
| `feat/follow` | seguir y dejar de seguir, followers, following y feed |
