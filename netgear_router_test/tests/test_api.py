import requests
from requests.auth import HTTPBasicAuth

def test_router_api(api_url, credentials):
    username, password = credentials
    try:
        response = requests.get(api_url, auth=HTTPBasicAuth(username, password), timeout=5)
        assert response.status_code == 200, f"API returned {response.status_code}"
    except requests.exceptions.RequestException as e:
        assert False, f"API request failed: {e}"
