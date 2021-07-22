#!/usr/bin/python3
from tabulate import tabulate
from serial.tools.list_ports import comports


def get_port():
    """ Return Detected Ports """
    ports = []
    for port in comports():
        description = port.description.lower()
        if description != 'n/a':
            ports.append([port.device, port.product, port.manufacturer])
    return ports


if __name__ == '__main__':
    ports = get_port()
    if len(ports) > 0:
        print(tabulate(
            ports,
            tablefmt='orgtbl',
            headers=[
                'Device',
                'Product',
                'Manufacturer']))
    else:
        print("No port avaiable!")
