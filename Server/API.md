# Culinary Notetaker API

Base URL: `http://127.0.0.1:8000`

## Authentication

Protected endpoints require a JWT access token:

```http
Authorization: Bearer <access_token>
```

Access tokens expire after 30 minutes. Use the refresh token to obtain a new access token.

---

## Auth (`/api/auth/`)

### Register

`POST /api/auth/register/`

**Auth:** None

**Request body:**
```json
{
  "username": "andrew",
  "password": "password123"
}
```

**Response:** `201 Created`
```json
{
  "user": {
    "id": 1,
    "username": "andrew",
    "profile": {
      "created_at": "2026-06-12T18:00:00Z",
      "updated_at": "2026-06-12T18:00:00Z"
    }
  },
  "tokens": {
    "access": "<jwt>",
    "refresh": "<jwt>"
  }
}
```

---

### Login

`POST /api/auth/login/`

**Auth:** None

**Request body:**
```json
{
  "username": "andrew",
  "password": "password123"
}
```

**Response:** `200 OK` — same shape as register (`user` + `tokens`).

---

### Refresh token

`POST /api/auth/token/refresh/`

**Auth:** None

**Request body:**
```json
{
  "refresh": "<refresh_token>"
}
```

**Response:** `200 OK`
```json
{
  "access": "<new_jwt>",
  "refresh": "<new_jwt>"
}
```

---

### Logout

`POST /api/auth/logout/`

**Auth:** Required

**Response:** `204 No Content`

Discard tokens on the client after logout.

---

### Get current user

`GET /api/auth/user/`

**Auth:** Required

**Response:** `200 OK`
```json
{
  "id": 1,
  "username": "andrew",
  "profile": {
    "created_at": "2026-06-12T18:00:00Z",
    "updated_at": "2026-06-12T18:00:00Z"
  }
}
```

---

### Update current user

`PATCH /api/auth/user/`

**Auth:** Required

**Request body:**
```json
{
  "username": "andrew2"
}
```

**Response:** `200 OK` — same shape as get user.

---

## Recipes (`/api/recipes/`)

All recipe endpoints return only recipes owned by the authenticated user.

### List recipes

`GET /api/recipes/`

**Auth:** Required

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "dish_name": "Pasta Carbonara",
    "cuisine_area": "Italian",
    "steps": ["Boil pasta", "Combine"],
    "ingredients": [
      {"name": "spaghetti", "amount": "400g"},
      {"name": "eggs", "amount": "4"}
    ],
    "created_at": "2026-06-12T18:00:00Z",
    "updated_at": "2026-06-12T18:00:00Z"
  }
]
```

---

### Create recipe

`POST /api/recipes/`

**Auth:** Required

**Request body:**
```json
{
  "dish_name": "Pasta Carbonara",
  "cuisine_area": "Italian",
  "steps": ["Boil pasta", "Mix eggs and cheese", "Combine"],
  "ingredients": [
    {"name": "spaghetti", "amount": "400g"},
    {"name": "eggs", "amount": "4"}
  ]
}
```

**Response:** `201 Created` — single recipe object.

---

### Get recipe

`GET /api/recipes/{id}/`

**Auth:** Required

**Response:** `200 OK` — single recipe object.

---

### Update recipe

`PUT /api/recipes/{id}/` — full replace

`PATCH /api/recipes/{id}/` — partial update

**Auth:** Required

**Request body:** same fields as create.

**Response:** `200 OK` — single recipe object.

---

### Delete recipe

`DELETE /api/recipes/{id}/`

**Auth:** Required

**Response:** `204 No Content`

---

## Recipe logs (`/api/recipes/`)

### List logs for a recipe

`GET /api/recipes/{recipe_id}/logs/`

**Auth:** Required

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "recipe_id": 3,
    "notes": "Added more salt",
    "date": "2026-06-12",
    "created_at": "2026-06-12T18:00:00Z"
  }
]
```

---

### Create recipe log

`POST /api/recipes/{recipe_id}/logs/`

**Auth:** Required

**Request body:**
```json
{
  "notes": "Added more salt",
  "date": "2026-06-12"
}
```

**Response:** `201 Created` — single log object.

---

### Update recipe log

`PUT /api/recipes/logs/{pk}/` — full replace

`PATCH /api/recipes/logs/{pk}/` — partial update

**Auth:** Required

**Request body:**
```json
{
  "notes": "Updated notes",
  "date": "2026-06-13"
}
```

**Response:** `200 OK` — single log object.

---

### Delete recipe log

`DELETE /api/recipes/logs/{pk}/`

**Auth:** Required

**Response:** `204 No Content`

---

## Cookbooks (`/api/cookbooks/`)

All cookbook endpoints return only cookbooks owned by the authenticated user.

### List cookbooks

`GET /api/cookbooks/`

**Auth:** Required

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "book_name": "Weeknight Dinners",
    "description": "Quick meals under 30 minutes",
    "recipe_ids": [3, 5],
    "created_at": "2026-06-12T18:00:00Z",
    "updated_at": "2026-06-12T18:00:00Z"
  }
]
```

---

### Create cookbook

`POST /api/cookbooks/`

**Auth:** Required

**Request body:**
```json
{
  "book_name": "Weeknight Dinners",
  "description": "Quick meals under 30 minutes"
}
```

**Response:** `201 Created` — single cookbook object.

---

### Get cookbook

`GET /api/cookbooks/{id}/`

**Auth:** Required

**Response:** `200 OK` — single cookbook object.

---

### Update cookbook

`PUT /api/cookbooks/{id}/` — full replace

`PATCH /api/cookbooks/{id}/` — partial update

**Auth:** Required

**Request body:**
```json
{
  "book_name": "Sunday Meals",
  "description": "Longer cooks for the weekend"
}
```

**Response:** `200 OK` — single cookbook object.

---

### Delete cookbook

`DELETE /api/cookbooks/{id}/`

**Auth:** Required

**Response:** `204 No Content`

---

## Cookbook recipes (`/api/cookbooks/`)

Many-to-many links between cookbooks and recipes.

### List recipes in a cookbook

`GET /api/cookbooks/{cookbook_id}/recipes/`

**Auth:** Required (cookbook must belong to current user)

**Response:** `200 OK`
```json
[
  {"recipe_id": 3},
  {"recipe_id": 5}
]
```

---

### Add recipe to cookbook

`POST /api/cookbooks/{cookbook_id}/recipes/`

**Auth:** Required (cookbook must belong to current user)

**Request body:**
```json
{
  "recipe_id": 3
}
```

**Response:** `201 Created`
```json
{"recipe_id": 3}
```

**Error:** `400 Bad Request` if the recipe is already in the cookbook.

---

### Remove recipe from cookbook

`DELETE /api/cookbooks/{cookbook_id}/recipes/{recipe_id}/`

**Auth:** Required (cookbook must belong to current user)

**Response:** `204 No Content`

---

## Common errors

| Status | When |
|--------|------|
| `400` | Invalid request body or validation failure |
| `401` | Missing or invalid JWT |
| `404` | Resource not found |

Validation errors return JSON with field names and error messages, e.g.:
```json
{
  "password": ["Ensure this field has at least 8 characters."]
}
```
