import requests
import json
from js_analyzer import analyze_js
from endpoint_mapper import analyze_endpoints


def fetch_html(url):
    try:
        r = requests.get(url, timeout=10)
        print(f"\n[+] Status Code: {r.status_code}")

        if r.status_code != 200:
            return None

        return r.text

    except Exception as e:
        print(f"[-] Error: {e}")
        return None


def save_report(data):
    with open("report.json", "w") as f:
        json.dump(data, f, indent=4)

    print("\n[+] Report saved → report.json")


def main():
    print("=== HackerRecon v4.1 (Clean Intelligence) ===")

    url = input("Enter URL: ").strip()

    if not url.startswith("http"):
        print("[-] Invalid URL")
        return

    html = fetch_html(url)
    if not html:
        return

    endpoints = analyze_js(html, url)
    if not endpoints:
        return

    report = analyze_endpoints(endpoints)

    save_report(report)


if __name__ == "__main__":
    main()