# Tasks API

A tiny to-do list REST API in Python and Flask. It is the running example for the **DevOps track on [agentlabs learn](https://learning.myagentlabs.ai)**: every course adds one layer to this same project, from running it on your laptop to Git, Docker, Compose, CI, nginx, the cloud and Kubernetes.

## Get the code

    git clone https://github.com/agl-learn-examples/devops-tasks-api.git tasks-api
    cd tasks-api

## Run it

    python3 -m venv .venv
    . .venv/bin/activate
    pip install -r requirements.txt
    flask --app app run

Then, in a second terminal:

    curl localhost:5000/health

Stop the server with Ctrl+C.

## Endpoints

| method | path | does |
|---|---|---|
| GET | /health | `{"status": "ok"}` |
| GET | /tasks | list tasks |
| POST | /tasks | create a task: `{"title": "...", "priority": "high"}` → 201 (priority: low, normal or high; default normal) |
| GET | /tasks/&lt;id&gt; | one task, or 404 |
| PUT | /tasks/&lt;id&gt; | replace a task |
| DELETE | /tasks/&lt;id&gt; | delete a task → 204 |

## Tests

    pytest

Run the tests inside the virtual environment, after `pip install`.

Tasks are stored in `tasks.db` (SQLite) next to `app.py`. If yours was made before tasks had a priority, delete it and it is made again.

## Pull requests

Pull requests are squash-merged: each one lands on `main` as one commit. No write access? Fork the repository, add the original as `upstream`, and rebase on `upstream/main` before you open a pull request.
