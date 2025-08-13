# 04 — Service Scanner

## 📌 What it does
Scans a **target IP address** over a range of ports and also **identifies the service running** on each open port using `socket.getservbyport()`.

This adds a practical layer to a port scan — knowing which service is running helps prioritise security checks.

---

## 🛠 How to run
```bash
macOS/Linux: python3 service_scanner.py
Windows: python service_scanner.py
