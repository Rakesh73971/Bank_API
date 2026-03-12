
def test_create_bank(client):

    data = {
        "name": "State Bank"
    }

    response = client.post("/banks", json=data)

    assert response.status_code == 201
    assert response.json()["name"] == "State Bank"

def test_get_all_banks(client):

    response = client.get("/banks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_bank_by_id(client):

    # First create bank
    data = {"name": "HDFC"}

    create_response = client.post("/banks", json=data)

    bank_id = create_response.json()["id"]

    # Fetch created bank
    response = client.get(f"/banks/{bank_id}")

    assert response.status_code == 200
    assert response.json()["name"] == "HDFC"

def test_get_bank_branches(client):

    bank = client.post("/banks/", json={"name": "Axis"})
    bank_id = bank.json()["id"]

    client.post("/branches/", json={
        "branch_name": "Axis Branch 1",
        "city":"Hyderabad",
        "ifsc": "AXIS0001",
        "bank_id": bank_id
    })

    client.post("/branches/", json={
        "branch_name": "Axis Branch 2",
        "city":"rangareddy",
        "ifsc": "AXIS0002",
        "bank_id": bank_id
    })

    response = client.get(f"/banks/{bank_id}/branches")

def test_bank_not_found(client):

    response = client.get("/banks/99999")

    assert response.status_code == 404