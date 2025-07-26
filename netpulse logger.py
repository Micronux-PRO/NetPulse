import os
import datetime
import speedtest
import pandas as pd

# 🔧 Ensure data folder exists
os.makedirs("data", exist_ok=True)

# 🕒 Timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 📶 Run speed test
try:
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Mbps
    upload_speed = st.upload() / 1_000_000      # Mbps
    ping = st.results.ping                     # ms

    # 🧾 Build log entry
    df = pd.DataFrame([{
        "Timestamp": timestamp,
        "Ping (ms)": round(ping, 2),
        "Download (Mbps)": round(download_speed, 2),
        "Upload (Mbps)": round(upload_speed, 2)
    }])

    # 💾 Log to CSV
    df.to_csv("data/logs.csv", mode="a", header=not os.path.exists("data/logs.csv"), index=False)
    print(f"✅ Logged speed test at {timestamp}")
    print(df)

except Exception as e:
    print(f"❌ Speed test failed: {e}")