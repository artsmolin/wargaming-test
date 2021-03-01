async def test_get_fibonacci_invalid(client):
    resp = await client.get('/fibonachi')
    assert resp.status == 400


async def test_get_fibonacci(client):
    resp = await client.get('/fibonachi', params={'from': 0, 'to': 5})
    assert resp.status == 200
    data = await resp.json()
    assert data['items'] == [1, 1, 2, 3, 5]
