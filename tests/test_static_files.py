def test_css_http_ok(app, client):
    response = client.get("/static/styles.css")
    assert response.status_code == 200

    response = client.get("/static/normalize.css")
    assert response.status_code == 200


def test_img_http_ok(app, client):
    response = client.get("/static/img/GitHub-Mark-64px.png")
    assert response.status_code == 200
