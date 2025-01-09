import socket

def get_open_ports(target, port_range):
    open_ports = []

    for port in range(port_range[0], port_range[1] + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            if sock.connect_ex((target, port)) == 0:
                open_ports.append(port)

    return open_ports

if __name__ == "__main__":
    print(get_open_ports("", []))
