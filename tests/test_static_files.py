def test_css_http_ok(client):
    response = client.get("/static/css/styles.css")
    assert response.status_code == 200

    response = client.get("/static/css/normalize.css")
    assert response.status_code == 200


def test_img_http_ok(client):
    response = client.get("/static/img/GitHub-Mark-64px.png")
    assert response.status_code == 200
