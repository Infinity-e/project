# 🔍 Simple Python Port Scanner

A lightweight Python script to scan TCP ports and resolve hostnames/IPs using only the built-in `socket` module. Perfect for learning networking basics, practicing recon, or building into larger cybersecurity tools.

---

## ✨ Features

- 🔎 Scan single or multiple TCP ports on a target.
- 🌐 Resolve domain names to IP addresses.
- 🧠 Lookup hostnames from IP addresses (reverse DNS).
- ✅ Clean, beginner-friendly code with basic error handling.

---

## 📦 Requirements

- Python 3.x
- No external libraries required — uses only Python’s built-in `socket` module.

---

## 🧠 How It Works

The script contains two core functions:

### 🔸 `port_scan(host, port)`
- Connects to a single TCP port using `socket()`.
- Prints:
  - IP address of the host.
  - Hostname of the IP (reverse DNS).
  - Port status (open/closed).

### 🔸 `prtscans(host, ports)`
- Takes a host and a list/tuple of ports.
- Resolves host to IP.
- Attempts reverse DNS.
- Iterates through each port and uses `port_scan()`.

---

## 💻 How to Use

1. Save the following code as `port_scanner.py`.
2. Run using:

```bash
python port_scanner.py
