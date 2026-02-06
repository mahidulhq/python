import speedtest
import sys
import time

print("Initializing speed test...", flush=True)
st = speedtest.Speedtest()

print("Selecting best server...", flush=True)
st.get_best_server()

print("Testing download speed (this takes ~20s)...", flush=True)
download_speed = st.download() / 1_000_000

print("Testing upload speed (this takes ~15s)...", flush=True)
upload_speed = st.upload() / 1_000_000

ping = st.results.ping
print(f"\n--- RESULTS ---")
print(f"Download: {download_speed:.2f} Mbps")
print(f"Upload: {upload_speed:.2f} Mbps")
print(f"Ping: {ping:.2f} ms")