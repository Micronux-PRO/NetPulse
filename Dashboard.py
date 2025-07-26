import pandas as pd
import matplotlib.pyplot as plt
import speedtest
from datetime import datetime

# 📡 Run live speed test
st = speedtest.Speedtest()
download = st.download() / 1_000_000  # Convert to Mbps
upload = st.upload() / 1_000_000      # Convert to Mbps
timestamp = datetime.now()

# 🧾 Create DataFrame with one entry
df = pd.DataFrame([{
    'Date': timestamp,
    'Download': round(download, 2),
    'Upload': round(upload, 2)
}])

# 📊 Plot Download and Upload speeds
plt.plot(df['Date'], df['Download'], label='Download Speed', marker='o', linestyle='--', color='blue')
plt.plot(df['Date'], df['Upload'], label='Upload Speed', marker='x', linestyle=':', color='green')

# 🎨 Style the graph
plt.title('Live NetPulse Speed Test')
plt.xlabel('Time')
plt.ylabel('Speed (Mbps)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left')
plt.tight_layout()

# 💾 Save and show
plt.savefig('netpulse_live_speed.png', dpi=300)
plt.show()