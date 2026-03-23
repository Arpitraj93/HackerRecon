import re
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import requests


def is_valid_endpoint(ep, base_url):
    ep = ep.strip()

    if ep.startswith("http"):
        base_domain = urlparse(base_url).netloc
        target_domain = urlparse(ep).netloc

        if not target_domain.endswith(base_domain):
            return False

        ep = urlparse(ep).path

    ep = ep.lower()

    junk = ['/', '/g', '/?', '//', '/.']
    if ep in junk or len(ep) < 4:
        return False

    noise = ['w3.org', 'doubleclick', 'cloudflare', 'googletag', 'analytics']
    if any(n in ep for n in noise):
        return False

    high_value = ['api', 'user', 'admin', 'rest', 'login', 'auth']
    if any(h in ep for h in high_value):
        return True

    if '?' in ep or '=' in ep:
        return True

    if any(v in ep for v in ['/v1/', '/v2/', '/v3/', '/graphql']):
        return True

    if ep.count('/') <= 7:
        return True

    return False


def analyze_js(html, base_url):
    print("\n[+] JavaScript Analysis Started...\n")

    soup = BeautifulSoup(html, "html.parser")
    scripts = soup.find_all("script")

    js_files = []

    for script in scripts:
        src = script.get("src")
        if src:
            js_files.append(urljoin(base_url, src))

    print(f"[+] Found {len(js_files)} JS files\n")

    endpoints = []

    for js in js_files:
        print(f"[+] Analyzing: {js}")

        try:
            r = requests.get(js, timeout=10)
            if r.status_code != 200:
                continue

            content = r.text

            matches = re.findall(
                r'["\'](\/(?:api|rest|graphql|v1|v2)[a-zA-Z0-9_\-\/\?=&]*)',
                content
            )

            for m in matches:
                if is_valid_endpoint(m, base_url):
                    print(f"    → {m}")
                    endpoints.append(m)

        except:
            pass

    endpoints = list(set(endpoints))

    print("\n[!] Cleaned Endpoints:")
    for ep in endpoints:
        print(f"  - {ep}")

    return endpoints