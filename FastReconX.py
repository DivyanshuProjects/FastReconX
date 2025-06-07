import socket
import requests
import argparse
import threading
import platform
import sys

import pyfiglet


def print_color(text, color_code):
    color_start = f"\033[{color_code}m"
    reset_color = "\033[0m"
    print(f"{color_start}{text}{reset_color}")
res = pyfiglet.figlet_format("FastreconX", width=100)

group = '''
Join the thriving community of Cyber Elite, where collective knowledge enhances
digital security, creating a robust and resilient online environment for all.

<!-- Project Name : FastReconX -->


'''
print_color(res, "91") 
print_color(group, "92") 

# ------------------- Fast Port Scanner (Multi-threaded) -------------------

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        sock.close()
    except:
        pass

def scan_ports_fast(target):
    print(f"\n[🔍] Scanning ports on {target} (1-1024) using -sT (TCP Connect)...")
    threads = []
    for port in range(1, 1025):
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

# ------------------- Subdomain Finder -------------------

def find_subdomains(domain):
    print(f"\n[🌐] Finding subdomains for {domain} using subdomains.txt...")
    try:
        with open("subdomains.txt", "r") as file:
            subdomains = file.read().splitlines()
    except FileNotFoundError:
        print("[!] subdomains.txt file not found.")
        return

    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            requests.get(url, timeout=3)
            print(f"[+] Found: {url}")
        except requests.ConnectionError:
            pass

# ------------------- Directory Fuzzer -------------------

def directory_fuzz(base_url):
    print(f"\n[📂] Fuzzing Directories at {base_url}")
    wordlist = ["admin", "login", "dashboard", "uploads", "images", "api", "config"]
    for word in wordlist:
        url = f"{base_url.rstrip('/')}/{word}"
        try:
            response = requests.get(url, timeout=3)
            if response.status_code not in [404, 403]:
                print(f"[+] Found: {url} - Status: {response.status_code}")
        except requests.RequestException:
            pass

# ------------------- Basic OS Detection -------------------

def os_detection(target):
    print(f"\n[🧠] Attempting basic OS detection for {target}...")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((target, 80))
        sock.send(b"HEAD / HTTP/1.1\r\nHost: target\r\n\r\n")
        banner = sock.recv(1024).decode(errors="ignore")
        print(f"[+] Banner:\n{banner}")
        if "Server:" in banner:
            print("[✓] Server header detected.")
        else:
            print("[!] No server header found.")
    except Exception as e:
        print(f"[!] OS Detection failed: {e}")
    finally:
        sock.close()

# ------------------- Run All -------------------
def run_all(target):
    scan_ports_fast(target)
    find_subdomains(target)
    directory_fuzz(f"http://{target}")
    os_detection(target)

# ------------------- Argument Parser -------------------
def main():
    parser = argparse.ArgumentParser(description="🛠️ Fast Recon Tool with OS Detection")
    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument("-a", "--all", action="store_true", help="Run all modules")
    parser.add_argument("-p", "--ports", action="store_true", help="Run fast -sT style port scan")
    parser.add_argument("-s", "--subfinder", action="store_true", help="Run subdomain discovery")
    parser.add_argument("-g", "--gobuster", action="store_true", help="Run directory brute-force")
    parser.add_argument("-o", "--osdetect", action="store_true", help="Run basic OS fingerprint")

    args = parser.parse_args()

    if args.all:
        run_all(args.target)
    else:
        if args.ports:
            scan_ports_fast(args.target)
        if args.subfinder:
            find_subdomains(args.target)
        if args.gobuster:
            directory_fuzz(f"http://{args.target}")
        if args.osdetect:
            os_detection(args.target)

    if not (args.all or args.ports or args.subfinder or args.gobuster or args.osdetect):
        print("[!] No module selected. Use -h for help.")

# ------------------- Entry -------------------
if __name__ == "__main__":
    main()
