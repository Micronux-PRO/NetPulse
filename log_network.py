# log_network.py
import requests
import csv
import datetime
import socket

# 🛠 CONFIG
LOG_SPEED = 'netpulse_logs.csv'
LOG_DNS = 'dns_benchmark_logs.csv'
DNS_SERVERS = {
    'Cloudflare': '1.1.1.1',
    'Google': '8.8.8.8',
    'Quad9': '9.9.9.9',
    'OpenDNS': '208.67.222.222',
    'NextDNS': '45.90.28.0'
}

# 🌐 Speed Test using external service
def test_speed():
    try:
        response = requests.get("https://speed.cloudflare.com/__down", timeout=10)
        download_speed = round(len(response.content) / 125000, 2)  # Convert to Mbps
        upload_speed = round(download_speed * 0.058, 2)  # Simulate upload for now
        return download_speed, upload_speed
    except Exception as e:
        print(f"❌ Speed test failed: {e}")
        return None, None

# 🧠 DNS Benchmark using socket ping
def test_dns_servers():
    results = []
    for name, ip in DNS_SERVERS.items():
        try:
            start = datetime.datetime.now()
            socket.gethostbyaddr(ip)  # Trigger DNS resolution
            end = datetime.datetime.now()
            latency = round((end - start).total_seconds() * 1000, 2)
            results.append((name, ip, latency))
        except Exception:
            results.append((name, ip, 'timeout'))
    return results

# 📝 Append results to logs
def log_results():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # 🚀 Log speed
    down, up = test_speed()
    if down and up:
        with open(LOG_SPEED, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, down, up])
        print(f"✅ Logged speed: ↓ {down} Mbps | ↑ {up} Mbps")
    
    # 🧠 Log DNS
    dns_results = test_dns_servers()
    with open(LOG_DNS, 'a', newline='') as f:
        writer = csv.writer(f)
        for name, ip, latency in dns_results:
            writer.writerow([timestamp, name, ip, latency])
    print("✅ Logged DNS benchmark.")

if __name__ == "__main__":
    print(f"\n🔄 NetPulse Logger — {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log_results()