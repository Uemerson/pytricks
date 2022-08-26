# Python 3 has a std lib
# module for working with
# IP addresses:

import ipaddress

print(ipaddress.ip_address("192.168.1.2"))
# output: IPv4Address("192.168.1.2")

print(ipaddress.ip_address("2001:af3::"))
# output: IPv6Address("2001:af3::")
