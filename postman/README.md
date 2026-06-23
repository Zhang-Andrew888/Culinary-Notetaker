# Postman API Tests

Importable Postman collection and environment for the Culinary Notetaker backend.

## Files

| File | Description |
|------|-------------|
| `Culinary_Notetaker.postman_collection.json` | All API requests with automated tests |
| `Culinary_Notetaker_Local.postman_environment.json` | Local dev variables (`base_url`, tokens, IDs) |

## Prerequisites

Start the Django server:

```bash
cd Server
./venv/bin/python manage.py migrate   # if DB is not set up
./venv/bin/python manage.py runserver
```

## Import into Postman

1. Open Postman
2. **Import** → drag both JSON files (or use File → Import)
3. Select the **Culinary Notetaker Local** environment (top-right dropdown)
4. Confirm `base_url` is `http://127.0.0.1:8000`

## How to run

### Option A: Full modular test run (recommended)

Run folders **in order** using Collection Runner:

1. `00_Setup` — register + login (sets `access_token`, `refresh_token`)
2. `01_Auth` — auth happy path + edge cases
3. `02_Recipes` — recipe CRUD + edge cases
4. `03_Recipe Logs` — log CRUD + edge cases
5. `04_Cookbooks` — cookbook CRUD + edge cases
6. `05_Cookbook Recipes` — M2M links + cleanup

Each request includes **Tests** that assert the expected HTTP status code and response shape. Successful creates save IDs to the environment (`recipe_id`, `log_id`, `cookbook_id`, etc.) for later requests.

### Option B: Single smoke test

Run folder **`06_Full Flow`** with Collection Runner — one end-to-end happy path from register through delete.

## Environment variables

| Variable | Purpose |
|----------|---------|
| `base_url` | API host |
| `username` / `password` | Test credentials |
| `unique_username` | Set automatically (username + timestamp) to avoid duplicate register errors |
| `access_token` / `refresh_token` | JWT tokens (set by register/login/refresh) |
| `recipe_id`, `log_id`, `cookbook_id` | Chained from create responses |
| `invalid_id` | `999999` for 404 tests |

## Regenerating the collection

If you change the API and update `generate_collection.py`:

```bash
cd postman
python3 generate_collection.py
```

Then re-import the collection in Postman.

## Expected status codes covered

| Code | Covered by |
|------|----------------|
| `200` | GET, PATCH, PUT, login, refresh |
| `201` | Register, create resources |
| `204` | Delete, logout |
| `400` | Validation errors (missing fields, duplicates, bad credentials) |
| `401` | Missing/invalid JWT |
| `404` | Resource not found |

See [`Server/API.md`](../Server/API.md) for full API documentation.
