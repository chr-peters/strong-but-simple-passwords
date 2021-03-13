def test_index_http_ok(client):
    response = client.get("/")
    assert response.status_code == 200
