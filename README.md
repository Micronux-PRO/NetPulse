# NetPulse
# 🚦 NetPulse: Internet Speed Logger & Analyzer

A minimalist and powerful tool for logging internet speed over time, benchmarking DNS performance, and generating reports to diagnose ISP issues or routing flaws.

Whether you're a gamer chasing stable ping, a streamer dodging lag spikes, or a digital worker tired of throttled uploads—NetPulse lets you track, visualize, and prove your network’s behavior.

---

## 🔧 Features

- 🕒 **Automated Speed Tests**  
  Logs ping, download, upload, and jitter at regular intervals.

- 📊 **Visual Performance Dashboard**  
  See trends, spikes, and averages using clean Matplotlib plots.

- 🌐 **DNS Benchmarking**  
  Compare latency across DNS providers and apply the best one.

- 📁 **Speed Report Generator**  
  Export daily or weekly logs as CSV or PDF—perfect for filing complaints or tracking improvements.

- 🧭 **Custom Ping Targets**  
  Add your favorite game servers or regional cities (e.g. Madrid, Lisbon) to trace routing issues.

---

## 🖥️ Installation

### Requirements
- Python 3.8+
- `speedtest-cli`
- `pandas`
- `matplotlib`
- *(Optional)* `reportlab` for PDF exports

### Setup
```bash
git clone https://github.com/your-username/NetPulse.git
cd NetPulse
pip install -r requirements.txt
python netpulse_logger.py
