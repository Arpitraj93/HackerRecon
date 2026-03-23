import requests

def fetch_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        print(f"\n[+] Status Code: {response.status_code}")

        return response

    except requests.exceptions.RequestException as e:
        print(f"[-] Request Error: {e}")
        return None