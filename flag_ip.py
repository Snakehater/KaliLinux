from time import sleep
#sleep(10)
import socket
hostname = socket.gethostname()
#IpAddr = socket.gethostbyname(hostname)

import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


IpAddr = get_ip_address('wlan0')
print 'Ip address is: ' + IpAddr

import requests
url = 'https://elvigo.com/vigor/API/RpiIp.php?ip='+IpAddr+'&hostname='+hostname

requests.get(url)
