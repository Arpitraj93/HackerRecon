from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup

def analyze(url, response):
    findings = []

    parsed = urlparse(url)
    params = parse_qs(parsed.query)

    if params:
        print("\n[+] Parameters Found:")
        for p in params:
            print(f"  - {p}")
            findings.append("parameter")
    else:
        print("\n[-] No parameters found")

    soup = BeautifulSoup(response.text, "html.parser")
    forms = soup.find_all("form")

    if forms:
        print("\n[+] Forms Found")
        findings.append("form")
    else:
        print("\n[-] No forms found")

    return findings