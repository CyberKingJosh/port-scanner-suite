# port-scanner-suite
🔐 Port Scanner Suite (Beginner SOC Project)
A progressive set of Python TCP scanners that grow from first principles to service/banner detection. Each step includes clear code, screenshots, and notes you can learn from.

🧭 What you’ll learn
Python sockets (TCP), timeouts, error handling

Loops, functions, lists, dictionaries (beginner-friendly)

Multi-target scanning and banner grabbing

Clean reporting (summaries, screenshots, READMEs)

📂 Project structure
projects/
port-scanner/
01-single-port/
  port_scanner_single.py
  README.md
  screenshots/
02-range-scanner/
03-multi-target/
04-service-banner/

Each subfolder contains:

README.md → what it does, how to run, key ideas

.py → the script

/screenshots → terminal outputs

▶️ Quick start
Run any version by navigating into its folder and:
python3 <scriptname>.py

Example safe targets:

127.0.0.1 (your machine)

scanme.nmap.org (small ranges only)

Example ports: 20–110

🔎 Versions
01 — Single Port → One IP, one port, open/closed check.
02 — Port Range → Scan a range on one host.
03 — Multi-Target → Same range across multiple hosts.
04 — Service + Banner → Show service names and try banner grabbing.

⚖️ Legal & Etiquette
Only scan systems you own or have permission to test.

Use small port ranges; respect network policies.

