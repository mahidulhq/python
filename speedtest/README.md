# Internet Speed Test CLI

Command-line internet speed tester using Speedtest.net servers.

## Python Libraries Used

- `speedtest` - Speedtest.net CLI wrapper
- `sys` - System-specific parameters
- `time` - Timing operations

## Features

- Auto-selects best Speedtest.net server
- Measures download/upload speeds (Mbps)
- Tests ping latency (ms)
- Real-time progress messages
- Formatted results display

## Installation

```bash
pip install speedtest-cli
python speedtest.py
```

## Usage

```bash
python speedtest.py
```

**Test duration**: ~35-45 seconds total

## Output Example

```
Initializing speed test...
Selecting best server...
Testing download speed (this takes ~20s)...
Testing upload speed (this takes ~15s)...

--- RESULTS ---
Download: 245.67 Mbps
Upload: 128.34 Mbps
Ping: 12.45 ms
```

## Code Flow

```
Init Speedtest → Best Server → Download Test → Upload Test → Ping → Results
```

## Server Selection

Automatically chooses optimal Speedtest.net server based on:
- Latency
- Jitter
- Packet loss

## Limitations

- Requires internet connection
- Console-only output
- Single test run
- No server selection override
- No historical data logging

***