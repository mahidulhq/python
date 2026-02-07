# Hostname to IP Resolver

Converts website domain names to IP addresses using DNS lookup.

## Python Libraries Used

- `socket` - Network socket operations and DNS resolution

## Features

- Interactive hostname input
- Single-command DNS A record lookup
- Error handling for invalid hostnames
- Displays specific socket error details

## Usage

```bash
python get.py
```

1. Enter website hostname (e.g., `google.com`)
2. Get corresponding IPv4 address

## Example

```
Website URL AKA Hostname: www.google.com
IP: 142.250.190.78

# Error case:
Website URL AKA Hostname: invalidxyz
Invalid Hostname, error raised is [Errno -2] Name or service not known
```

## Code Flow

```
Input hostname → socket.gethostbyname() → Print IP or Error
```

## Supported

- Domain names (google.com)
- Subdomains (www.github.com)
- IP addresses (returns unchanged)

## Limitations

- IPv4 only (A records)
- No IPv6 support
- Single hostname per run
- Basic error reporting only
- Console input/output

***