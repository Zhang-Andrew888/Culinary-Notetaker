#!/usr/bin/env python3
"""Generate Postman collection JSON for Culinary Notetaker API."""
import json
from pathlib import Path


def url(path_segments):
    parts = [p for seg in path_segments for p in seg.strip("/").split("/") if p]
    raw = "{{base_url}}/" + "/".join(parts) + "/"
    return {
        "raw": raw,
        "host": ["{{base_url}}"],
        "path": parts + [""],
    }


def json_body(data):
    return {
        "mode": "raw",
        "raw": json.dumps(data, indent=2),
        "options": {"raw": {"language": "json"}},
    }


def headers_json():
    return [{"key": "Content-Type", "value": "application/json"}]


def test_script(*lines):
    return [{"listen": "test", "script": {"type": "text/javascript", "exec": lines}}]


def pre_request_script(*lines):
    return [{"listen": "prerequest", "script": {"type": "text/javascript", "exec": lines}}]


def events(test_lines=None, pre_lines=None):
    ev = []
    if pre_lines:
        ev.extend(pre_request_script(*pre_lines))
    if test_lines:
        ev.extend(test_script(*test_lines))
    return ev


def req(name, method, path_parts, *, body=None, body_raw=None, auth_bearer=True, tests=None, prerequest=None):
    item = {
        "name": name,
        "request": {
            "method": method,
            "header": headers_json() if (body is not None or body_raw is not None) else [],
            "url": url(path_parts),
        },
    }
    if not auth_bearer:
        item["request"]["auth"] = {"type": "noauth"}
    if body_raw is not None:
        item["request"]["body"] = {
            "mode": "raw",
            "raw": body_raw,
            "options": {"raw": {"language": "json"}},
        }
    elif body is not None:
        item["request"]["body"] = json_body(body)
    ev = events(tests, prerequest)
    if ev:
        item["event"] = ev
    return item


def folder(name, items, *, auth_bearer=True):
    f = {"name": name, "item": items}
    if auth_bearer:
        f["auth"] = {
            "type": "bearer",
            "bearer": [{"key": "token", "value": "{{access_token}}", "type": "string"}],
        }
    return f


SAVE_TOKENS = [
    "pm.test('Status code matches', function () {",
    "    pm.expect(pm.response.code).to.be.oneOf([200, 201]);",
    "});",
    "const json = pm.response.json();",
    "if (json.tokens) {",
    "    pm.environment.set('access_token', json.tokens.access);",
    "    pm.environment.set('refresh_token', json.tokens.refresh);",
    "}",
    "if (json.user) {",
    "    pm.environment.set('user_id', json.user.id);",
    "}",
]

collection = {
    "info": {
        "_postman_id": "culinary-notetaker-api",
        "name": "Culinary Notetaker API",
        "description": "API tests for Culinary Notetaker backend. Import with Culinary Notetaker Local environment.",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
    },
    "auth": {
        "type": "bearer",
        "bearer": [{"key": "token", "value": "{{access_token}}", "type": "string"}],
    },
    "item": [
        folder(
            "00_Setup",
            [
                req(
                    "Register test user (201)",
                    "POST",
                    ["api", "auth", "register", ""],
                    auth_bearer=False,
                    body={"username": "{{unique_username}}", "password": "{{password}}"},
                    prerequest=[
                        "pm.environment.set('unique_username', pm.environment.get('username') + '_' + Date.now());",
                    ],
                    tests=[
                        "pm.test('Status is 201', function () { pm.response.to.have.status(201); });",
                        *SAVE_TOKENS,
                        "pm.test('User has profile', function () {",
                        "    pm.expect(pm.response.json().user.profile).to.be.an('object');",
                        "});",
                    ],
                ),
                req(
                    "Login test user (200)",
                    "POST",
                    ["api", "auth", "login", ""],
                    auth_bearer=False,
                    body={"username": "{{unique_username}}", "password": "{{password}}"},
                    tests=[
                        "pm.test('Status is 200', function () { pm.response.to.have.status(200); });",
                        *SAVE_TOKENS,
                    ],
                ),
            ],
            auth_bearer=False,
        ),
        folder(
            "01_Auth",
            [
                folder(
                    "Happy path",
                    [
                        req(
                            "Refresh token (200)",
                            "POST",
                            ["api", "auth", "token", "refresh", ""],
                            auth_bearer=False,
                            body={"refresh": "{{refresh_token}}"},
                            tests=[
                                "pm.test('Status is 200', function () { pm.response.to.have.status(200); });",
                                "const json = pm.response.json();",
                                "pm.test('Returns new access token', function () {",
                                "    pm.expect(json.access).to.be.a('string');",
                                "});",
                                "pm.environment.set('access_token', json.access);",
                                "if (json.refresh) { pm.environment.set('refresh_token', json.refresh); }",
                            ],
                        ),
                        req(
                            "Get current user (200)",
                            "GET",
                            ["api", "auth", "user", ""],
                            tests=[
                                "pm.test('Status is 200', function () { pm.response.to.have.status(200); });",
                                "const json = pm.response.json();",
                                "pm.test('Has id, username, profile', function () {",
                                "    pm.expect(json).to.have.keys('id', 'username', 'profile');",
                                "});",
                            ],
                        ),
                        req(
                            "Update user PATCH (200)",
                            "PATCH",
                            ["api", "auth", "user", ""],
                            body={"username": "{{unique_username}}"},
                            tests=[
                                "pm.test('Status is 200', function () { pm.response.to.have.status(200); });",
                                "pm.test('Username updated', function () {",
                                "    pm.expect(pm.response.json().username).to.eql(pm.environment.get('unique_username'));",
                                "});",
                            ],
                        ),
                        req(
                            "Logout (204)",
                            "POST",
                            ["api", "auth", "logout", ""],
                            tests=[
                                "pm.test('Status is 204', function () { pm.response.to.have.status(204); });",
                            ],
                        ),
                        req(
                            "Re-login after logout (200)",
                            "POST",
                            ["api", "auth", "login", ""],
                            auth_bearer=False,
                            body={"username": "{{unique_username}}", "password": "{{password}}"},
                            tests=[
                                "pm.test('Status is 200', function () { pm.response.to.have.status(200); });",
                                *SAVE_TOKENS,
                            ],
                        ),
                    ],
                    auth_bearer=False,
                ),
                folder(
                    "Edge cases",
                    [
                        req(
                            "Register - missing password (400)",
                            "POST",
                            ["api", "auth", "register", ""],
                            auth_bearer=False,
                            body={"username": "bad_user_no_pass"},
                            tests=[
                                "pm.test('Status is 400', function () { pm.response.to.have.status(400); });",
                            ],
                        ),
                        req(
                            "Register - short password (400)",
                            "POST",
                            ["api", "auth", "register", ""],
                            auth_bearer=False,
                            body={"username": "bad_user_short", "password": "short"},
                            tests=[
                                "pm.test('Status is 400', function () { pm.response.to.have.status(400); });",
                            ],
                        ),
                        req(
                            "Login - wrong password (400)",
                            "POST",
                            ["api", "auth", "login", ""],
                            auth_bearer=False,
                            body={"username": "{{unique_username}}", "password": "wrongpassword"},
                            tests=[
                                "pm.test('Status is 400', function () { pm.response.to.have.status(400); });",
                            ],
                        ),
                        req(
                            "Login - missing username (400)",
                            "POST",
                            ["api", "auth", "login", ""],
                            auth_bearer=False,
                            body={"password": "{{password}}"},
                            tests=[
                                "pm.test('Status is 400', function () { pm.response.to.have.status(400); });",
                            ],
                        ),
                        req(
                            "Refresh - invalid token (401)",
                            "POST",
                            ["api", "auth", "token", "refresh", ""],
                            auth_bearer=False,
                            body={"refresh": "invalid.token.here"},
                            tests=[
                                "pm.test('Status is 401', function () { pm.response.to.have.status(401); });",
                            ],
                        ),
                        req(
                            "Get user - no auth (401)",
                            "GET",
                            ["api", "auth", "user", ""],
                            auth_bearer=False,
                            tests=[
                                "pm.test('Status is 401', function () { pm.response.to.have.status(401); });",
                            ],
                        ),
                        req(
                            "Logout - no auth (401)",
                            "POST",
                            ["api", "auth", "logout", ""],
                            auth_bearer=False,
                            tests=[
                                "pm.test('Status is 401', function () { pm.response.to.have.status(401); });",
                            ],
                        ),
                    ],
                    auth_bearer=False,
                ),
            ],
            auth_bearer=False,
        ),
        folder(
            "02_Recipes",
            [
                folder(
                    "Happy path",
                    [
                        req(
                            "List recipes (200)",
                            "GET",
                            ["api", "recipes", ""],
                            tests=[
                                "pm.test('Status is 200', function () { pm.response.to.have.status(200); });",
                                "pm.test('Response is array', function () {",
                                "    pm.expect(pm.response.json()).to.be.an('array');",
                                "});",
                            ],
                        ),
                        req(
                            "Create recipe (201)",
                            "POST",
                            ["api", "recipes", ""],
                            body={
                                "dish_name": "Pasta Carbonara",
                                "cuisine_area": "Italian",
                                "steps": ["Boil pasta", "Mix eggs and cheese", "Combine"],
                                "ingredients": [
                                    {"name": "spaghetti", "amount": "400g"},
                                    {"name": "eggs", "amount": "4"},
                                ],
                            },
                            tests=[
                                "pm.test('Status is 201', function () { pm.response.to.have.status(201); });",
                                "pm.environment.set('recipe_id', pm.response.json().id);",
                                "pm.test('Has dish_name', function () {",
                                "    pm.expect(pm.response.json().dish_name).to.eql('Pasta Carbonara');",
                                "});",
                            ],
                        ),
                        req(
                            "Create second recipe (201)",
                            "POST",
                            ["api", "recipes", ""],
                            body={
                                "dish_name": "Greek Salad",
                                "cuisine_area": "Greek",
                                "steps": ["Chop vegetables", "Add dressing"],
                                "ingredients": [{"name": "feta", "amount": "100g"}],
                            },
                            tests=[
                                "pm.test('Status is 201', function () { pm.response.to.have.status(201); });",
                                "pm.environment.set('recipe_id_2', pm.response.json().id);",
                            ],
                        ),
                        req(
                            "Get recipe (200)",
                            "GET",
                            ["api", "recipes", "{{recipe_id}}", ""],
                            tests=[
                                "pm.test('Status is 200', function () { pm.response.to.have.status(200); });",
                                "pm.test('Correct recipe id', function () {",
                                "    pm.expect(pm.response.json().id).to.eql(parseInt(pm.environment.get('recipe_id')));",
                                "});",
                            ],
                        ),
                        req(
                            "PATCH recipe (200)",
                            "PATCH",
                            ["api", "recipes", "{{recipe_id}}", ""],
                            body={"cuisine_area": "Italian (updated)"},
                            tests=[
                                "pm.test('Status is 200', function () { pm.response.to.have.status(200); });",
                                "pm.test('Field updated', function () {",
                                "    pm.expect(pm.response.json().cuisine_area).to.eql('Italian (updated)');",
                                "});",
                            ],
                        ),
                        req(
                            "PUT recipe (200)",
                            "PUT",
                            ["api", "recipes", "{{recipe_id}}", ""],
                            body={
                                "dish_name": "Pasta Carbonara",
                                "cuisine_area": "Italian",
                                "steps": ["Boil pasta", "Combine"],
                                "ingredients": [{"name": "spaghetti", "amount": "400g"}],
                            },
                            tests=[
                                "pm.test('Status is 200', function () { pm.response.to.have.status(200); });",
                            ],
                        ),
                    ],
                ),
                folder(
                    "Edge cases",
                    [
                        req(
                            "List - no auth (401)",
                            "GET",
                            ["api", "recipes", ""],
                            auth_bearer=False,
                            tests=[
                                "pm.test('Status is 401', function () { pm.response.to.have.status(401); });",
                            ],
                        ),
                        req(
                            "Create - missing dish_name (400)",
                            "POST",
                            ["api", "recipes", ""],
                            body={"cuisine_area": "Italian", "steps": [], "ingredients": []},
                            tests=[
                                "pm.test('Status is 400', function () { pm.response.to.have.status(400); });",
                            ],
                        ),
                        req(
                            "Create - invalid ingredient (400)",
                            "POST",
                            ["api", "recipes", ""],
                            body={
                                "dish_name": "Bad Recipe",
                                "cuisine_area": "Test",
                                "steps": [],
                                "ingredients": [{"name": "flour"}],
                            },
                            tests=[
                                "pm.test('Status is 400', function () { pm.response.to.have.status(400); });",
                            ],
                        ),
                        req(
                            "Get - not found (404)",
                            "GET",
                            ["api", "recipes", "{{invalid_id}}", ""],
                            tests=[
                                "pm.test('Status is 404', function () { pm.response.to.have.status(404); });",
                            ],
                        ),
                        req(
                            "PATCH - not found (404)",
                            "PATCH",
                            ["api", "recipes", "{{invalid_id}}", ""],
                            body={"dish_name": "Ghost"},
                            tests=[
                                "pm.test('Status is 404', function () { pm.response.to.have.status(404); });",
                            ],
                        ),
                        req(
                            "DELETE - not found (404)",
                            "DELETE",
                            ["api", "recipes", "{{invalid_id}}", ""],
                            tests=[
                                "pm.test('Status is 404', function () { pm.response.to.have.status(404); });",
                            ],
                        ),
                        req(
                            "DELETE second recipe (204)",
                            "DELETE",
                            ["api", "recipes", "{{recipe_id_2}}", ""],
                            tests=[
                                "pm.test('Status is 204', function () { pm.response.to.have.status(204); });",
                            ],
                        ),
                    ],
                ),
            ],
        ),
        folder(
            "03_Recipe Logs",
            [
                folder(
                    "Happy path",
                    [
                        req(
                            "List logs (200)",
                            "GET",
                            ["api", "recipes", "{{recipe_id}}", "logs", ""],
                            tests=[
                                "pm.test('Status is 200', function () { pm.response.to.have.status(200); });",
                                "pm.test('Response is array', function () {",
                                "    pm.expect(pm.response.json()).to.be.an('array');",
                                "});",
                            ],
                        ),
                        req(
                            "Create log (201)",
                            "POST",
                            ["api", "recipes", "{{recipe_id}}", "logs", ""],
                            body={"notes": "Added more salt", "date": "2026-06-12"},
                            tests=[
                                "pm.test('Status is 201', function () { pm.response.to.have.status(201); });",
                                "pm.environment.set('log_id', pm.response.json().id);",
                            ],
                        ),
                        req(
                            "PATCH log (200)",
                            "PATCH",
                            ["api", "recipes", "logs", "{{log_id}}", ""],
                            body={"notes": "Updated notes"},
                            tests=[
                                "pm.test('Status is 200', function () { pm.response.to.have.status(200); });",
                                "pm.test('Notes updated', function () {",
                                "    pm.expect(pm.response.json().notes).to.eql('Updated notes');",
                                "});",
                            ],
                        ),
                        req(
                            "PUT log (200)",
                            "PUT",
                            ["api", "recipes", "logs", "{{log_id}}", ""],
                            body={"notes": "Full replace notes", "date": "2026-06-13"},
                            tests=[
                                "pm.test('Status is 200', function () { pm.response.to.have.status(200); });",
                            ],
                        ),
                    ],
                ),
                folder(
                    "Edge cases",
                    [
                        req(
                            "Create - missing date (400)",
                            "POST",
                            ["api", "recipes", "{{recipe_id}}", "logs", ""],
                            body={"notes": "No date"},
                            tests=[
                                "pm.test('Status is 400', function () { pm.response.to.have.status(400); });",
                            ],
                        ),
                        req(
                            "Create - no auth (401)",
                            "POST",
                            ["api", "recipes", "{{recipe_id}}", "logs", ""],
                            auth_bearer=False,
                            body={"notes": "Unauthorized", "date": "2026-06-12"},
                            tests=[
                                "pm.test('Status is 401', function () { pm.response.to.have.status(401); });",
                            ],
                        ),
                        req(
                            "PATCH - not found (404)",
                            "PATCH",
                            ["api", "recipes", "logs", "{{invalid_id}}", ""],
                            body={"notes": "Ghost"},
                            tests=[
                                "pm.test('Status is 404', function () { pm.response.to.have.status(404); });",
                            ],
                        ),
                        req(
                            "DELETE - not found (404)",
                            "DELETE",
                            ["api", "recipes", "logs", "{{invalid_id}}", ""],
                            tests=[
                                "pm.test('Status is 404', function () { pm.response.to.have.status(404); });",
                            ],
                        ),
                        req(
                            "DELETE log (204)",
                            "DELETE",
                            ["api", "recipes", "logs", "{{log_id}}", ""],
                            tests=[
                                "pm.test('Status is 204', function () { pm.response.to.have.status(204); });",
                            ],
                        ),
                    ],
                ),
            ],
        ),
        folder(
            "04_Cookbooks",
            [
                folder(
                    "Happy path",
                    [
                        req(
                            "List cookbooks (200)",
                            "GET",
                            ["api", "cookbooks", ""],
                            tests=[
                                "pm.test('Status is 200', function () { pm.response.to.have.status(200); });",
                                "pm.test('Response is array', function () {",
                                "    pm.expect(pm.response.json()).to.be.an('array');",
                                "});",
                            ],
                        ),
                        req(
                            "Create cookbook (201)",
                            "POST",
                            ["api", "cookbooks", ""],
                            body={
                                "book_name": "Weeknight Dinners",
                                "description": "Quick meals under 30 minutes",
                            },
                            tests=[
                                "pm.test('Status is 201', function () { pm.response.to.have.status(201); });",
                                "pm.environment.set('cookbook_id', pm.response.json().id);",
                            ],
                        ),
                        req(
                            "Get cookbook (200)",
                            "GET",
                            ["api", "cookbooks", "{{cookbook_id}}", ""],
                            tests=[
                                "pm.test('Status is 200', function () { pm.response.to.have.status(200); });",
                                "pm.test('Has recipe_ids', function () {",
                                "    pm.expect(pm.response.json().recipe_ids).to.be.an('array');",
                                "});",
                            ],
                        ),
                        req(
                            "PATCH cookbook (200)",
                            "PATCH",
                            ["api", "cookbooks", "{{cookbook_id}}", ""],
                            body={"description": "Updated description"},
                            tests=[
                                "pm.test('Status is 200', function () { pm.response.to.have.status(200); });",
                            ],
                        ),
                        req(
                            "PUT cookbook (200)",
                            "PUT",
                            ["api", "cookbooks", "{{cookbook_id}}", ""],
                            body={
                                "book_name": "Weeknight Dinners",
                                "description": "Full replace description",
                            },
                            tests=[
                                "pm.test('Status is 200', function () { pm.response.to.have.status(200); });",
                            ],
                        ),
                    ],
                ),
                folder(
                    "Edge cases",
                    [
                        req(
                            "Create - missing book_name (400)",
                            "POST",
                            ["api", "cookbooks", ""],
                            body={"description": "No name"},
                            tests=[
                                "pm.test('Status is 400', function () { pm.response.to.have.status(400); });",
                            ],
                        ),
                        req(
                            "Get - not found (404)",
                            "GET",
                            ["api", "cookbooks", "{{invalid_id}}", ""],
                            tests=[
                                "pm.test('Status is 404', function () { pm.response.to.have.status(404); });",
                            ],
                        ),
                        req(
                            "Get - no auth (401)",
                            "GET",
                            ["api", "cookbooks", "{{cookbook_id}}", ""],
                            auth_bearer=False,
                            tests=[
                                "pm.test('Status is 401', function () { pm.response.to.have.status(401); });",
                            ],
                        ),
                        req(
                            "DELETE - not found (404)",
                            "DELETE",
                            ["api", "cookbooks", "{{invalid_id}}", ""],
                            tests=[
                                "pm.test('Status is 404', function () { pm.response.to.have.status(404); });",
                            ],
                        ),
                    ],
                ),
            ],
        ),
        folder(
            "05_Cookbook Recipes",
            [
                folder(
                    "Happy path",
                    [
                        req(
                            "List recipes in cookbook (200)",
                            "GET",
                            ["api", "cookbooks", "{{cookbook_id}}", "recipes", ""],
                            tests=[
                                "pm.test('Status is 200', function () { pm.response.to.have.status(200); });",
                                "pm.test('Response is array', function () {",
                                "    pm.expect(pm.response.json()).to.be.an('array');",
                                "});",
                            ],
                        ),
                        req(
                            "Add recipe to cookbook (201)",
                            "POST",
                            ["api", "cookbooks", "{{cookbook_id}}", "recipes", ""],
                            body_raw='{\n  "recipe_id": {{recipe_id}}\n}',
                            tests=[
                                "pm.test('Status is 201', function () { pm.response.to.have.status(201); });",
                                "pm.test('Returns recipe_id', function () {",
                                "    pm.expect(pm.response.json().recipe_id).to.eql(parseInt(pm.environment.get('recipe_id')));",
                                "});",
                            ],
                        ),
                        req(
                            "List recipes again (200)",
                            "GET",
                            ["api", "cookbooks", "{{cookbook_id}}", "recipes", ""],
                            tests=[
                                "pm.test('Status is 200', function () { pm.response.to.have.status(200); });",
                                "pm.test('Contains recipe', function () {",
                                "    const ids = pm.response.json().map(r => r.recipe_id);",
                                "    pm.expect(ids).to.include(parseInt(pm.environment.get('recipe_id')));",
                                "});",
                            ],
                        ),
                    ],
                ),
                folder(
                    "Edge cases",
                    [
                        req(
                            "Add duplicate recipe (400)",
                            "POST",
                            ["api", "cookbooks", "{{cookbook_id}}", "recipes", ""],
                            body_raw='{\n  "recipe_id": {{recipe_id}}\n}',
                            tests=[
                                "pm.test('Status is 400', function () { pm.response.to.have.status(400); });",
                            ],
                        ),
                        req(
                            "Add - missing recipe_id (400)",
                            "POST",
                            ["api", "cookbooks", "{{cookbook_id}}", "recipes", ""],
                            body={},
                            tests=[
                                "pm.test('Status is 400', function () { pm.response.to.have.status(400); });",
                            ],
                        ),
                        req(
                            "List - cookbook not found (404)",
                            "GET",
                            ["api", "cookbooks", "{{invalid_id}}", "recipes", ""],
                            tests=[
                                "pm.test('Status is 404', function () { pm.response.to.have.status(404); });",
                            ],
                        ),
                        req(
                            "Remove recipe (204)",
                            "DELETE",
                            ["api", "cookbooks", "{{cookbook_id}}", "recipes", "{{recipe_id}}", ""],
                            tests=[
                                "pm.test('Status is 204', function () { pm.response.to.have.status(204); });",
                            ],
                        ),
                        req(
                            "Remove - not in cookbook (404)",
                            "DELETE",
                            ["api", "cookbooks", "{{cookbook_id}}", "recipes", "{{recipe_id}}", ""],
                            tests=[
                                "pm.test('Status is 404', function () { pm.response.to.have.status(404); });",
                            ],
                        ),
                    ],
                ),
                folder(
                    "Cleanup",
                    [
                        req(
                            "Delete cookbook (204)",
                            "DELETE",
                            ["api", "cookbooks", "{{cookbook_id}}", ""],
                            tests=[
                                "pm.test('Status is 204', function () { pm.response.to.have.status(204); });",
                            ],
                        ),
                    ],
                ),
            ],
        ),
        folder(
            "06_Full Flow",
            [
                req(
                    "1. Register (201)",
                    "POST",
                    ["api", "auth", "register", ""],
                    auth_bearer=False,
                    body={"username": "{{unique_username}}", "password": "{{password}}"},
                    prerequest=[
                        "pm.environment.set('unique_username', 'flow_' + pm.environment.get('username') + '_' + Date.now());",
                    ],
                    tests=[
                        "pm.test('Status is 201', function () { pm.response.to.have.status(201); });",
                        *SAVE_TOKENS,
                    ],
                ),
                req(
                    "2. Create recipe (201)",
                    "POST",
                    ["api", "recipes", ""],
                    body={
                        "dish_name": "Flow Test Recipe",
                        "cuisine_area": "Test",
                        "steps": ["Step 1"],
                        "ingredients": [{"name": "test", "amount": "1"}],
                    },
                    tests=[
                        "pm.test('Status is 201', function () { pm.response.to.have.status(201); });",
                        "pm.environment.set('recipe_id', pm.response.json().id);",
                    ],
                ),
                req(
                    "3. Create log (201)",
                    "POST",
                    ["api", "recipes", "{{recipe_id}}", "logs", ""],
                    body={"notes": "Flow log", "date": "2026-06-12"},
                    tests=[
                        "pm.test('Status is 201', function () { pm.response.to.have.status(201); });",
                        "pm.environment.set('log_id', pm.response.json().id);",
                    ],
                ),
                req(
                    "4. Create cookbook (201)",
                    "POST",
                    ["api", "cookbooks", ""],
                    body={"book_name": "Flow Cookbook", "description": "Smoke test"},
                    tests=[
                        "pm.test('Status is 201', function () { pm.response.to.have.status(201); });",
                        "pm.environment.set('cookbook_id', pm.response.json().id);",
                    ],
                ),
                req(
                    "5. Add recipe to cookbook (201)",
                    "POST",
                    ["api", "cookbooks", "{{cookbook_id}}", "recipes", ""],
                    body_raw='{\n  "recipe_id": {{recipe_id}}\n}',
                    tests=[
                        "pm.test('Status is 201', function () { pm.response.to.have.status(201); });",
                    ],
                ),
                req(
                    "6. List recipes (200)",
                    "GET",
                    ["api", "recipes", ""],
                    tests=[
                        "pm.test('Status is 200', function () { pm.response.to.have.status(200); });",
                    ],
                ),
                req(
                    "7. Delete log (204)",
                    "DELETE",
                    ["api", "recipes", "logs", "{{log_id}}", ""],
                    tests=[
                        "pm.test('Status is 204', function () { pm.response.to.have.status(204); });",
                    ],
                ),
                req(
                    "8. Remove recipe from cookbook (204)",
                    "DELETE",
                    ["api", "cookbooks", "{{cookbook_id}}", "recipes", "{{recipe_id}}", ""],
                    tests=[
                        "pm.test('Status is 204', function () { pm.response.to.have.status(204); });",
                    ],
                ),
                req(
                    "9. Delete cookbook (204)",
                    "DELETE",
                    ["api", "cookbooks", "{{cookbook_id}}", ""],
                    tests=[
                        "pm.test('Status is 204', function () { pm.response.to.have.status(204); });",
                    ],
                ),
                req(
                    "10. Delete recipe (204)",
                    "DELETE",
                    ["api", "recipes", "{{recipe_id}}", ""],
                    tests=[
                        "pm.test('Status is 204', function () { pm.response.to.have.status(204); });",
                    ],
                ),
            ],
        ),
    ],
}

out = Path(__file__).parent / "Culinary_Notetaker.postman_collection.json"
out.write_text(json.dumps(collection, indent=2))
print(f"Wrote {out}")
