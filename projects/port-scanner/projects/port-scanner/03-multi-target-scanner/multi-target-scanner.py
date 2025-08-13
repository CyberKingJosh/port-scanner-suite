import socket
import time

def scan_host(target_ip_or_name, start_port, end_port):
    print(f"\n🔍 Scanning target: {target_ip_or_name}")
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        try:
            s.connect((target_ip_or_name, port))
            print(f"[OPEN] {target_ip_or_name}:{port}")
        except:
            pass
        finally:
            s.close()
    time.sleep(0.5)

def main():
    print("=== Multi-Target Port Scanner (Beginner Edition) ===")
    targets = [
        "127.0.0.1",
        "scanme.nmap.org",
        "example.com"
    ]
    try:
        start_port = int(input("Start port (e.g., 20): ").strip())
        end_port   = int(input("End port   (e.g., 110): ").strip())
    except ValueError:
        print("Please enter whole numbers for ports.")
        return
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Port range must be 1..65535 and start <= end.")
        return
    t0 = time.time()
    for target in targets:
        scan_host(target, start_port, end_port)
    total_time = time.time() - t0
    print(f"\n✅ Done. Scanned {len(targets)} target(s) in {total_time:.2f} seconds.")

if __name__ == "__main__":
    main()
