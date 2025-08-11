import socket
target_ip = input("Enter the target IP address: ")
port = int(input("Enter the port number: "))
s = socket.socket()
s.settimeout(1)
try:
    s.connect((target_ip, port))
    print(f"[OPEN] Port {port} is open on {target_ip}")
except:
   print(f"[CLOSED] Port {port} is closed or filtered")
finally:
    s.close()
