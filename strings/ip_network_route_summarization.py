"""IP Network: Route Summarization
An IP network is a set of routers that communicate routing information using a protocol.
A router is uniquely identified by an IP address.
In IPv4, an IP address consists of 32 bits, canonically represented as 4 decimal numbers of 8 bits each.
The decimal numbers range from 0 (00000000) to 255 (11111111).
Each router has a "routing table" that contains a list of IP addresses, for the router to know where to send IP packets.

Route summarization in IP networks
As the network grows large (hundreds of routers), the number of IP addresses in the routing table increases rapidly.
Maintaining a high number of IP addresses in the routing table would result in a loss of performances
(memory, bandwidth and CPU resources limitation).
Route summarization, also called route aggregation,
consists in reducing the number of routes by aggregating them into a "summary route".

Let's consider the following example:
summary route

We have 4 routers connected to A. A is aware about all 4 IP addresses,
because it has a direct interface to each of them. However, A will not send them all to B.
Instead, it will aggregate the addresses into a summary route, and send this new route to B.
This implies that:

- Less bandwidth is used on the link between A and B.
- B saves memory: it has only one route to store in its routing table
- B saves CPU resources: there are less entries to consider when handling incoming IP packets
Computing a summary route
A has all 4 addresses stored in its routing table.

Address 1	172.16.12.0
Address 2	172.16.13.0
Address 3	172.16.14.0
Address 4	172.16.15.0

A will convert these IP addresses to binary format,
align them and find the boundary line between the common prefix on the left (highlighted in red),
and the remaining bits on the right.

Address 1	10101100	00010000	00001100	00000000
Address 2	10101100	00010000	00001101	00000000
Address 3	10101100	00010000	00001110	00000000
Address 4	10101100	00010000	00001111	00000000

A creates a new IP address made of the common bits, and all other bits set to "0".
This new IP address is converted back to decimal numbers.
Finally, A computes the number of common bits, also called "subnet".
The summary route is this new IP address, followed by a slash and the subnet: 172.16.12.0/22

Input: A list of strings containing the IP addresses
Output: A string containing the summary route, represented as an IP address, followed by a slash and the subnet.

Example:
checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"
checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"
checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"

Preconditions:
all(re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",d) for d in data))
all(-1 < int(n) < 256 for n in d.split(".") for d in data)
len(data) == len(set(data)) and len(data) > 1
"""
from typing import List, Iterable


def longest_common_prefix(strings: Iterable[str]):
    """ return the longest common prefix string amongst an array of strings """
    prefix = ''
    for string in zip(*strings):
        if len(set(string)) != 1:
            break
        prefix += string[0]
    return prefix


# v1
def checkio(ip_addresses: List[str]) -> str:
    """ Computing a summary route """
    binary_ip_addresses = (''.join(format(int(byte), '008b') for byte in ip.split('.')) for ip in ip_addresses)
    route = longest_common_prefix(binary_ip_addresses)
    subnet = len(route)
    route = route.ljust(32, '0')
    return f'{int(route[:8], base=2)}.' \
           f'{int(route[8:16], base=2)}.' \
           f'{int(route[16:24], base=2)}.' \
           f'{int(route[24:], base=2)}/{subnet}'


# v2
def checkio(ip_addresses: List[str]) -> str:
    """ Computing a summary route """
    binary_ip_addresses = (''.join(format(int(byte), '008b') for byte in ip.split('.')) for ip in ip_addresses)
    route = longest_common_prefix(binary_ip_addresses)
    subnet = len(route)
    route = route.ljust(32, '0')
    return f'{".".join(str(int(route[i:i + 8], base=2)) for i in range(0, 32, 8))}/{subnet}'


if __name__ == '__main__':
    print(checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]))
    print(checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]))
    print(checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"), "Second Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"), "Third Test"
