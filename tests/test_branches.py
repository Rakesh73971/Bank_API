
def test_get_branches(client):
    response = client.get('/branches')

    assert response.status_code == 200
