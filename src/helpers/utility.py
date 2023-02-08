import requests

def _make_post_request(url, api_key, payload):
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {api_key}"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f'Error: {response.status_code}: {response.content}')