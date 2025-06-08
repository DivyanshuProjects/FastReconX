 _____         _                           __  __
|  ___|_ _ ___| |_ _ __ ___  ___ ___  _ __ \ \/ /
| |_ / _` / __| __| '__/ _ \/ __/ _ \| '_ \ \  /
|  _| (_| \__ \ |_| | |  __/ (_| (_) | | | |/  \
|_|  \__,_|___/\__|_|  \___|\___\___/|_| |_/_/\_\



FastReconX is a fast, multi-functional reconnaissance tool designed for security professionals and bug bounty hunters. It combines port scanning, subdomain enumeration, directory fuzzing, and basic OS fingerprinting into a single easy-to-use CLI tool.

---

 Features

- ⚡ Fast multi-threaded TCP Connect port scanning** (ports 1-1024)
- 🌐 Subdomain discovery** using a customizable `subdomains.txt` wordlist
- 📂 Directory brute-forcing** with a built-in wordlist for common directories
- 🧠 Basic OS detection** via banner grabbing and fingerprinting

---


Join the thriving community of Cyber Elite, where collective knowledge enhances
digital security, creating a robust and resilient online environment for all.

<!-- Project Name : FastReconX -->

usage: Checking-making.py [-h] [-a] [-p] [-s] [-g] [-o] target

🛠️ Fast Recon Tool with OS Detection

positional arguments:
  target           Target IP or domain

options:
  -h, --help       show this help message and exit
  -a, --all        Run all modules
  -p, --ports      Run fast -sT style port scan
  -s, --subfinder  Run subdomain discovery
  -g, --gobuster   Run directory brute-force
  -o, --osdetect   Run basic OS fingerprint

 Installation

1. Make sure you have Python 3 installed.

2. Clone or download this repository.

3. Ensure you have the `requests` library installed:

   
   pip install requests
