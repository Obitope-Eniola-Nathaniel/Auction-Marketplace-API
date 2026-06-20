# Auction Marketplace API

A backend service that allows users to create auctions and place bids.

## Tech Stack

- Python 3
- Django
- Django REST Framework
- PostgreSQL
- Simple JWT
- drf-spectacular for Swagger/OpenAPI
- pytest

## Project Structure

The codebase is organized by domain under `apps/`:

- `apps.users` handles registration, authentication, and roles.
- `apps.auctions` will handle auction listings.
- `apps.bids` will handle bids and bid history.
- `apps.common` stores shared base models, permissions, exceptions, and utilities.

Configuration lives in `config/settings/`:

- `base.py` contains shared settings.
- `local.py` is used for development.
- `production.py` is used for deployment.

## Local Setup

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements\local.txt
Copy-Item .env.example .env
python manage.py migrate
python manage.py runserver
```

Local development uses SQLite by default so you can start quickly. Production settings use PostgreSQL through `config.settings.production`.

## API Docs

After starting the server, open:

- `http://127.0.0.1:8000/api/docs/`
- `http://127.0.0.1:8000/api/schema/`

## Current Auth Endpoints

- `POST /api/auth/register/`
- `POST /api/auth/login/`
- `POST /api/auth/refresh/`
