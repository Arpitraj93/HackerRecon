from urllib.parse import urlparse
from knowledge_loader import load_knowledge

# Load knowledge base once
kb = load_knowledge()


def use_knowledge(code, server=""):
    code = str(code)

    if code in kb:
        # Handle special case (cloudflare)
        if "cloudflare" in server and "cloudflare" in kb[code]:
            data = kb[code]["cloudflare"]
        else:
            data = kb[code].get("default", [])

        print("\n[+] Knowledge-Based Insights:\n")
        for line in data:
            print(line)
        print()


def interpret_response(response, url):
    code = response.status_code
    headers = response.headers
    server = headers.get("Server", "").lower()

    print(f"\n[+] Status Code: {code}")

    # Extract domain
    domain = urlparse(url).netloc

    # -----------------------------
    if code == 200:
        print("\n→ Meaning: Application accessible")

        print("\n→ Basic Recon Commands:")
        print(f"  curl -I {url}")
        print(f"  whatweb {url}")
        print(f"  gau {domain}")

        print("\n→ Next:")
        print("  - Analyze JavaScript files")
        print("  - Check API calls in DevTools")

    # -----------------------------
    elif code == 403:
        print("\n→ Meaning: Access forbidden")

        print("\n→ Basic Checks:")
        print(f"  curl -I {url}")
        print(f"  curl -H 'User-Agent: Mozilla/5.0' {url}")

        # 🔥 Use knowledge base here
        use_knowledge(403, server)

    # -----------------------------
    elif code == 500:
        print("\n→ Meaning: Server error")

        print("\n→ Basic Testing:")
        print("  - Try sending unexpected input")
        print("  - Test parameters for injection")

        # 🔥 Knowledge base
        use_knowledge(500)

    # -----------------------------
    else:
        print("\n→ Meaning: Unknown response")
        print("→ Manual investigation required\n")