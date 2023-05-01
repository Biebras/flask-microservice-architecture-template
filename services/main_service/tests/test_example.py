def test_example(client):
    response = client.get('/get_service_1')
    assert response.status_code == 200