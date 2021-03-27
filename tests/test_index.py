from strong_but_simple_passwords.core import sentences


def test_index_http_ok(client):
    response = client.get("/")
    assert response.status_code == 200


def test_empty_post(client):
    response = client.post("/")

    is_sentence_in = [cur_sentence in str(response.data) for cur_sentence in sentences]

    assert response.status_code == 200
    assert any(is_sentence_in)


def test_strong_password(client):
    payload = {"input_sentence": "A very long input sentence for a strong password"}
    response = client.post("/", data=payload)

    assert response.status_code == 200
    assert b"Congratulations!" in response.data
    assert b"centuries" in response.data
