import socket
import collections
import netifaces

def connect(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.01)
    result = sock.connect_ex((hostname, port))
    sock.close()
    return result == 0

def get_network_printer_ip():
    printer_list = collections.deque()
    data = None

    ifaces =netifaces.interfaces()
    print(ifaces)
    addrs = netifaces.ifaddresses('wlp4s0')
    add = addrs[2][0]["addr"]
    print(add)
    space = add.split(".")
    space = space[0] + "." + space[1] + "." + space[2] + "."

    for i in range(0, 255):
        if space + str(i) != add:
            res = connect(space+str(i), 9100)

            if res:
                print("Device found at: " + space + str(i) + ":"+str(9100))
                printer_list.append(space + str(i))

    print(printer_list)
    return printer_list

x = get_network_printer()
