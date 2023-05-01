def test_get_example(client):
    response = client.get('/service_1/api_1')
    assert response.status_code == 200
    
def test_post_example(client):
    data = {"key": "value"}
    response = client.post('/service_1/api_2', json=data)
    assert response.status_code == 200