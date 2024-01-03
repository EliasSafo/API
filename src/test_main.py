from fastapi.testclient import TestClient

from main import app

client = TestClient(app)
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello World"

def test_delete_all_stores():
    response = client.put("/stores/")
    assert response.status_code == 200
    assert response.json()["message"] == "All stores deleted"

def test_create_and_delete_stores():
    store_data = {"email": "test@test.com", "name": "John Doe"}
    response = client.post("/stores", json=store_data)
    assert response.status_code == 200
    assert response.json() == store_data["email"]
    assert response.json() == store_data["name"]
    response = client.put("/stores/")
    assert response.status_code == 200
    assert response.json()["message"] == "All stores deleted"
    assert response.json().get("email") is None

def test_update_store_address():
    store_data = {"email": "test@test.com", "name": "John Doe"}
    response = client.post("/stores", json=store_data)
    assert response.status_code == 200
    assert response.json()["email"] == store_data["email"]
    assert response.json()["name"] == store_data["name"]
    id = response.json().get("id")
    update_data = {"new_address": "new_test@test.com", "id": id}
    response = client.put(f"/stores/{id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["id"] == id
    assert response.json()["email"] == update_data["new_address"]
    assert response.json()["name"] == store_data["email"]
