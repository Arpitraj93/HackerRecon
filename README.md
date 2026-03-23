# HackerRecon – Web Attack Surface Analyzer

## What is this?

HackerRecon is a simple Python tool I built to make web reconnaissance easier.

While practicing web security, I realized that finding hidden endpoints manually (especially inside JavaScript files) takes a lot of time and it's easy to miss important things.  
So I created this tool to automate that process and highlight the parts that actually matter.

---

## What does it do?

In simple terms, it helps you:

- Find hidden endpoints from JavaScript files
- Discover API routes that are not visible directly
- Identify potentially sensitive or interesting paths
- Filter out useless data
- Highlight endpoints that look more risky
- Suggest what kind of attacks you can try (like IDOR, auth bypass, etc.)

---

## Why I built this

During labs and practice (TryHackMe, HTB, etc.), I noticed:

- A lot of endpoints are hidden in JS files  
- Manual recon is slow  
- It's hard to decide *where to focus first*

So instead of just collecting data, I wanted a tool that:
👉 finds endpoints  
👉 analyzes them  
👉 tells me where to look first  

---

## How to install

```bash
git clone git@github.com:Arpitraj93/HackerRecon.git
cd HackerRecon
pip install -r requirements.txt

---


## Use this tool as you want but for educational purpose and must me authorized target .
