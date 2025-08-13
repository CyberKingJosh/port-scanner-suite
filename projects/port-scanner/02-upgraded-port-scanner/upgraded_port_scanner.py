import socket
targets_ip = input("Enter the ip address: ")
start_port=int(input("what is the start of the port you want to search for: "))
End_port=int(input("What is the end of the port you want me to go through: "))
for port in range(start_port,End_port + 1):
    s = socket.socket()
    s.settimeout(1)
    try: 
        s.connect((targets_ip,port))
        print(f"[OPEN] Port {port} is open")
    except:
        print(f"[CLOSED] Port {port} is closed or filtered")
    finally:
        s.close()
