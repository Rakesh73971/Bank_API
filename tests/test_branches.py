
def test_get_branches(client):
    response = client.get('/branches')

    assert response.status_code == 200

def test_create_branch(client):

    # First create a bank because branch needs bank_id
    bank_data = {"name": "HDFC"}

    bank_response = client.post("/banks/", json=bank_data)

    bank_id = bank_response.json()["id"]

    branch_data = {

        "branch_name": "HDFC Hyderabad",
        "city":"Hyderabad",
        "ifsc": "HDFC0001",
        "bank_id": bank_id
    }

    response = client.post("/branches/", json=branch_data)

    assert response.status_code == 201
    assert response.json()["branch_name"] == "HDFC Hyderabad"
    assert response.json()["bank_id"] == bank_id

def test_get_branch_by_id(client):

    bank = client.post("/banks/", json={"name": "ICICI"})
    bank_id = bank.json()["id"]

    branch = client.post("/branches/", json={
        "branch_name": "ICICI Main",
        "city":"Chennai",
        "ifsc": "ICICI0001",
        "bank_id": bank_id
    })

    branch_id = branch.json()["id"]

    response = client.get(f"/branches/{branch_id}")

    assert response.status_code == 200
    assert response.json()["id"] == branch_id