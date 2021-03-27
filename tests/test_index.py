from strong_but_simple_passwords import views


def test_index_http_ok(client):
    response = client.get("/")
    assert response.status_code == 200


def test_empty_post(monkeypatch, client):
    a_random_sentence = "A random sentence."
    monkeypatch.setattr(views, "get_random_sentence", lambda: a_random_sentence)

    response = client.post("/")

    assert response.status_code == 200
    assert a_random_sentence in str(response.data)


def test_strong_password(client):
    payload = {"input_sentence": "A very long input sentence for a strong password"}
    response = client.post("/", data=payload)

    assert response.status_code == 200
    assert b"Congratulations!" in response.data
    assert b"centuries" in response.data
