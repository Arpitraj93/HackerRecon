def generate_report(findings):
    print("\n=========== REPORT ===========\n")

    if not findings:
        print("[!] No attack surface found in HTML\n")

        print("→ Likely Scenario:")
        print("  - JavaScript-based app")
        print("  - API-driven backend")
        print("  - Authentication required\n")

        print("→ Next Steps:")
        print("  - Open DevTools → Network tab")
        print("  - Capture API endpoints")
        print("  - Use Burp Suite to intercept traffic\n")

        return

    for f in set(findings):
        if f == "parameter":
            print("[!] Parameters Found")
            print("→ Test:")
            print("  ?id=1' OR 1=1--")
            print("  ?id=../../etc/passwd\n")

        elif f == "form":
            print("[!] Forms Found")
            print("→ Test:")
            print("  ' OR 1=1--")
            print("  <script>alert(1)</script>\n")