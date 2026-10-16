import pytest
import app as tasks_app


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)          # tasks.db is made in a fresh folder for each test
    return tasks_app.app.test_client()


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}


def test_create_and_list(client):
    r = client.post("/tasks", json={"title": "learn HTTP"})
    assert r.status_code == 201
    assert client.get("/tasks").get_json() == [{"id": 1, "title": "learn HTTP", "done": False}]


def test_title_required(client):
    assert client.post("/tasks", json={}).status_code == 400


def test_missing_task_is_404(client):
    assert client.get("/tasks/99").status_code == 404


def test_delete_is_204(client):
    client.post("/tasks", json={"title": "x"})
    assert client.delete("/tasks/1").status_code == 204
