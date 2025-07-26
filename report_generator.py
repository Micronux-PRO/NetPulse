# report_generator.py
import pandas as pd
from datetime import datetime

LOG_SPEED = 'netpulse_logs.csv'
LOG_DNS = 'dns_benchmark_logs.csv'

def summarize_speed():
    try:
        # Speed log CSV has no header, so we define it manually
        df = pd.read_csv(LOG_SPEED, header=None, names=['Date', 'Download', 'Upload'])
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df['Download'] = pd.to_numeric(df['Download'], errors='coerce')
        df['Upload'] = pd.to_numeric(df['Upload'], errors='coerce')
        df.dropna(inplace=True)

        latest = df.iloc[-1]
        avg_down = df['Download'].mean()
        avg_up = df['Upload'].mean()

        print("🚀 Internet Speed Summary")
        print(f"Latest Test: {latest['Date']}")
        print(f"↓ Download: {latest['Download']} Mbps")
        print(f"↑ Upload:   {latest['Upload']} Mbps")
        print(f"📊 Averages — ↓ {avg_down:.2f} Mbps | ↑ {avg_up:.2f} Mbps")

    except Exception as e:
        print(f"❌ Failed to summarize speed log: {e}")

def summarize_dns():
    try:
        # DNS log CSV has no header, so we define it manually
        df = pd.read_csv(LOG_DNS, header=None, names=['Timestamp', 'DNS Server', 'IP', 'Latency (ms)'])
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
        df.dropna(subset=['Timestamp'], inplace=True)

        latest_time = df['Timestamp'].max()
        latest = df[df['Timestamp'] == latest_time]

        print("\n🧠 DNS Benchmark Summary")
        for _, row in latest.iterrows():
            latency = row['Latency (ms)']
            if str(latency).lower() == 'timeout':
                print(f"{row['DNS Server']} ({row['IP']}) ➜ ❌ Timeout")
            else:
                print(f"{row['DNS Server']} ({row['IP']}) ➜ ✅ {latency} ms")

    except Exception as e:
        print(f"❌ Failed to summarize DNS log: {e}")

if __name__ == "__main__":
    print(f"\n📅 NetPulse Report — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    summarize_speed()
    summarize_dns()