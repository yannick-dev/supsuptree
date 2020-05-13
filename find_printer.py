from os import listdir


# returns the path of the connected escpos printer or 404 if none is connected

def get_usb_printer_path():
    directories = listdir("/dev/usb")
    print(dir)
    for direcectory in directories:
        if direcectory[0] == 'l':
            path = '/dev/usb/' + direcectory
            print(path)
            serial = open(path, 'wb')
            serial.write(b'\x10\x04\x01')
            serial.close()
            serial = open(path, 'rb')
            answer = serial.read()
            serial.close()
            print(type(answer))
            print(answer)
            print("b'" + "\\x16'")
            if str(answer) == "b'" + "\\x16'":
                return path

    return "404"
