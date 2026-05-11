# sicnpcf-backend

Backend del SICNPCF: Django 5 + DRF + Celery, 16 apps (12 modulos del contrato + 4 fundacionales).

## Apps

Fundacionales: `core`, `users`, `audit`, `documents`
Modulos: `firma` (Mod 4), `oficialia` (Mod 1), `expediente` (Mod 2), `turnado` (Mod 3),
         `audiencias` (Mod 5), `notificaciones` (Mod 6), `exhortos` (Mod 7),
         `juicios_esp` (Mod 8), `registros` (Mod 9), `juicio_linea` (Mod 10),
         `tribunal_2a` (Mod 11), `estadistica` (Mod 12)

## Desarrollo

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements/dev.txt
python manage.py migrate
python manage.py runserver
```

O con Docker desde el container repo: `make up`.
