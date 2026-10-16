# Tasks API

A tiny to-do list REST API in Python and Flask. It is the running example for the **DevOps track on [agentlabs learn](https://learning.myagentlabs.ai)**: every course adds one layer to this same project, from running it on your laptop to Git, Docker, Compose, CI, nginx, the cloud and Kubernetes.

## Run it

    python3 -m venv .venv
    . .venv/bin/activate
    pip install -r requirements.txt
    flask --app app run

Then, in a second terminal:

    curl localhost:5000/health

## Endpoints

| method | path | does |
|---|---|---|
| GET | /health | `{"status": "ok"}` |
| GET | /tasks | list tasks |
| POST | /tasks | create a task: `{"title": "..."}` → 201 |
| GET | /tasks/&lt;id&gt; | one task, or 404 |
| PUT | /tasks/&lt;id&gt; | replace a task |
| DELETE | /tasks/&lt;id&gt; | delete a task → 204 |

## Tests

    pytest

Tasks are stored in `tasks.db` (SQLite) next to `app.py`.

## Errors

Errors come back as JSON: `{"error": "..."}` with 400 (bad input) or 404 (no such task).
