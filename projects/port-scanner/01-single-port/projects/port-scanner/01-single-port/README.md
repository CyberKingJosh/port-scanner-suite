01 — Single-Port Scanner

What: Connects to one IP and one port; prints OPEN or CLOSED/FILTERED.
Why: First principles—socket connect, timeout, and safe cleanup.

How to run
- macOS/Linux: python3 port_scanner_single.py
- Windows:     python port_scanner_single.py

Good test targets
- 127.0.0.1 (your machine)
- scanme.nmap.org (permissioned demo host)

Example ports: 20–110

Key ideas
- One TCP socket per check
- Short timeout to avoid hangs
- Clear open/closed output

