import socket
import time

COMMON_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}

def grab_banner(ip: str, port: int) -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    try:
        s.connect((ip, port))
        probe = b""
        if port == 80:
            probe = f"HEAD / HTTP/1.0\r\nHost: {ip}\r\n\r\n".encode()
        elif port in (22, 25, 110, 143):
            probe = b""
        elif port == 443:
            probe = b""
        if probe:
            try:
                s.sendall(probe)
            except OSError:
                pass
        try:
            data = s.recv(1024)
        except socket.timeout:
            data = b""
        banner = data.decode(errors="ignore").strip()
        return banner
    except (socket.timeout, ConnectionRefusedError, OSError):
        return ""
    finally:
        s.close()

def check_port(ip: str, port: int) -> tuple[bool, str, str]:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.8)
    try:
        s.connect((ip, port))
        is_open = True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return (False, "", "")
    finally:
        s.close()
    service_name = COMMON_SERVICES.get(port, "unknown")
    banner = grab_banner(ip, port)
    return (is_open, service_name, banner)

def scan_host(ip_or_name: str, start_port: int, end_port: int) -> dict:
    print(f"\n🔍 Scanning: {ip_or_name}")
    open_ports = []
    open_count = 0
    for port in range(start_port, end_port + 1):
        is_open, service_name, banner = check_port(ip_or_name, port)
        if is_open:
            open_count += 1
            open_ports.append(port)
            if banner:
                print(f"[OPEN] {ip_or_name}:{port} ({service_name})  |  Banner: {banner}")
            else:
                print(f"[OPEN] {ip_or_name}:{port} ({service_name})  |  (no readable banner)")
    time.sleep(0.5)
    return {"host": ip_or_name, "open_count": open_count, "open_ports": open_ports}

def main():
    print("=== Service Scanner with Banners (Beginner Edition) ===")
    targets = [
        "127.0.0.1",
        "scanme.nmap.org"
    ]
    try:
        start_port = int(input("Start port (e.g., 20): ").strip())
        end_port   = int(input("End port   (e.g., 110): ").strip())
    except ValueError:
        print("Ports must be whole numbers.")
        return
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Port range must be 1..65535 and start <= end.")
        return
    t0 = time.time()
    results = []
    for target in targets:
        summary = scan_host(target, start_port, end_port)
        results.append(summary)
    total_time = time.time() - t0
    print("\n===== SUMMARY =====")
    for item in results:
        host = item["host"]
        count = item["open_count"]
        ports_list = item["open_ports"]
        print(f"{host}: {count} open port(s) → {ports_list if ports_list else '[]'}")
    print(f"Scan finished in {total_time:.2f} seconds.")
    print("Note: Only scan systems you own or have permission to test.")

if __name__ == "__main__":
    main()
