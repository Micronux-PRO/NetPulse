# dns_benchmark.py
import socket
import time
import csv
from datetime import datetime

DNS_SERVERS = {
    "Cloudflare": "1.1.1.1",
    "Google": "8.8.8.8",
    "Quad9": "9.9.9.9",
    "OpenDNS": "208.67.222.222",
    "NextDNS": "45.90.28.0"
}

PORT = 53
TIMEOUT = 2  # seconds
LOG_FILE = "dns_benchmark_logs.csv"

def benchmark_dns(server_ip):
    start = time.time()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(TIMEOUT)
        sock.connect((server_ip, PORT))
        latency = round((time.time() - start) * 1000, 2)  # in ms
        sock.close()
        return latency
    except Exception:
        return None

def log_results(results):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    header = ['Timestamp', 'DNS Server', 'IP', 'Latency (ms)']
    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        for dns_name, latency in results.items():
            writer.writerow([timestamp, dns_name, DNS_SERVERS[dns_name], latency if latency is not None else 'Timeout'])

def run_benchmark():
    results = {}
    print("🔧 Benchmarking DNS servers...")
    for name, ip in DNS_SERVERS.items():
        latency = benchmark_dns(ip)
        results[name] = latency
        print(f"{name} ({ip}) ➜ {latency if latency else 'Timeout'} ms")
    log_results(results)
    print(f"\n✅ Results logged to '{LOG_FILE}'.")

if __name__ == "__main__":
    run_benchmark()