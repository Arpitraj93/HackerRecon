def score_endpoint(endpoint):
    ep = endpoint.lower()
    score = 0

    if "/api" in ep or "/rest" in ep:
        score += 4

    if "login" in ep or "auth" in ep:
        score += 3

    if "admin" in ep:
        score += 4

    if "?" in ep or "=" in ep:
        score += 3

    sensitive = ['user', 'account', 'order', 'cart', 'profile', 'password']
    if any(s in ep for s in sensitive):
        score += 2

    return score


def suggest_attack(endpoint):
    ep = endpoint.lower()

    # 🔥 IDOR
    if "id=" in ep or "uid=" in ep or "user_id=" in ep:
        return {
            "type": "IDOR",
            "steps": [
                f"Modify ID in request → {endpoint}",
                "Try accessing other user data",
                "Check for unauthorized data access"
            ]
        }

    # 🔥 LOGIN
    elif "login" in ep:
        return {
            "type": "Auth Attack",
            "steps": [
                "Intercept login request in Burp Suite",
                "Send to Intruder",
                "Use common password wordlist",
                "Check for weak authentication"
            ]
        }

    # 🔥 PASSWORD RESET
    elif "reset" in ep or "password" in ep:
        return {
            "type": "Account Takeover",
            "steps": [
                "Intercept reset request",
                "Modify token/email",
                "Check for missing validation",
                "Test token reuse"
            ]
        }

    # 🔥 ADMIN
    elif "admin" in ep:
        return {
            "type": "Access Control",
            "steps": [
                f"Try accessing directly → {endpoint}",
                "Check without authentication",
                "Test privilege escalation"
            ]
        }

    # 🔥 PARAM FUZZING
    elif "?" in endpoint:
        return {
            "type": "Parameter Fuzzing",
            "steps": [
                f'ffuf -u "{endpoint}FUZZ" -w /usr/share/wordlists/dirb/common.txt',
                "Check for unexpected responses",
                "Look for IDOR or injection"
            ]
        }

    # 🔥 API FUZZING
    elif "/api" in ep or "/rest" in ep:
        clean_ep = endpoint.rstrip('/')
        return {
            "type": "API Fuzzing",
            "steps": [
                f"ffuf -u {clean_ep}/FUZZ -w /usr/share/wordlists/dirb/common.txt",
                "Look for hidden endpoints",
                "Check response differences"
            ]
        }

    else:
        return {
            "type": "Manual Testing",
            "steps": [
                "Analyze request manually in Burp Suite"
            ]
        }


def analyze_endpoints(endpoints):
    print("\n[+] Attack Intelligence (Top Targets):\n")

    results = []

    for ep in endpoints:
        score = score_endpoint(ep)
        attack_info = suggest_attack(ep)
        results.append((score, ep, attack_info))

    # 🔥 Sort highest first
    results.sort(reverse=True)

    report = []

    for score, ep, attack_info in results:
        if score < 5:
            continue

        print(f"[🔥] {ep} (Score: {score}/10)")
        print(f"   [Attack Type] {attack_info['type']}")
        print("   [Steps]")

        for step in attack_info["steps"]:
            print(f"     - {step}")

        print()

        report.append({
            "endpoint": ep,
            "score": score,
            "attack_type": attack_info["type"],
            "steps": attack_info["steps"]
        })

    return report