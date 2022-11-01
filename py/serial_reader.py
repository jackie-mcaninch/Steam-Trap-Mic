import serial
import matplotlib.pyplot as plt
import sys
import time

# USAGE: python3 py/serial_reader.py <COM_PORT> <NUM_SECS> <NUM_POINTS>

com_port = sys.argv[1]
num_secs = float(sys.argv[2]) if len(sys.argv) > 2 else 5
num_pts = int(sys.argv[3]) if len(sys.argv) > 3 else 100*num_secs
resolution = num_secs / num_pts
ser = serial.Serial(com_port, 115200, timeout=1)
data = []
hist_threshold = 100
peak_diffs = []
devs = []
peak_threshold = 3.3

start = time.time()
t = time.time() - start
datum = 0
ser.readline()
while t < num_secs:
    try:
        datum = float(ser.readline().decode('utf-8').strip())
    except ValueError: pass # just use last recorded datum
    data.append((datum, t))
    # if len(data) >= hist_threshold:
    #     latest = [d for d,t in data[-hist_threshold:]]
    #     peak_diffs.append((max(latest)-min(latest), t))
    t = time.time() - start

plt.xlabel("Time since start (s)")
plt.ylabel("Voltage")
plt.plot([t for (d,t) in data], [d for (d,t) in data], color="blue")
# plt.plot([t for (p,t) in peak_diffs], [p for (p,t) in peak_diffs], color="red")
# plt.plot([t for (s,t) in devs], [s for (s,t) in devs], color="green")
plt.show()