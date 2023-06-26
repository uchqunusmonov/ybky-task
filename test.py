import requests
params = {'search': 'workly'}
response = requests.get('https://uchqunusmonov.jprq.live/api/rooms/', params)
assert response.status_code == 200
print(response.text)

data = response.json()
assert "page" in data
assert "count" in data
assert "page_size" in data
assert "results" in data

results = data["results"]
assert isinstance(results, list)

for room in results:
    assert "id" in room
    assert "name" in room
    assert "type" in room
    assert "capacity" in room
    print(room["name"])
    # assert room["name"] == "workly"