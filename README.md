# InterviewVault
Full-stack interview question library: Django REST Framework + React/Vite + PostgreSQL (SQLite fallback).

## Features
- JWT registration/login, logout in frontend
- Search, company/topic/difficulty filters, sorting
- Submit questions with company, job role, and round
- Duplicate question normalization and reports
- Responsive dashboard, statistics, loading/error/empty states
- Django admin

## Run backend (PowerShell)
```powershell
cd backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
python manage.py makemigrations accounts companies experiences questions
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Leave `DB_NAME` blank in `.env` for SQLite. For PostgreSQL, fill `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`.

## Run frontend (second terminal)
```powershell
cd frontend
npm install
npm run dev
```
Open http://localhost:5173. API: http://127.0.0.1:8000/api/health/ . Admin: http://127.0.0.1:8000/admin/.

Never commit `.env` or real secrets. For production, use HTTPS, secure refresh-token handling, rate limiting, and a production secret key.
