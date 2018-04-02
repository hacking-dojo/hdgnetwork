# -*- coding: utf-8 -*-

"""
Module docstring
"""
import socket
import struct
import re


class Whois():

    ABUSEHOST = "whois.abuse.net"
    NICHOST = "whois.crsnic.net"
    INICHOST = "whois.networksolutions.com"
    DNICHOST = "whois.nic.mil"
    GNICHOST = "whois.nic.gov"
    ANICHOST = "whois.arin.net"
    LNICHOST = "whois.lacnic.net"
    RNICHOST = "whois.ripe.net"
    PNICHOST = "whois.apnic.net"
    MNICHOST = "whois.ra.net"
    QNICHOST_TAIL = ".whois-servers.net"
    SNICHOST = "whois.6bone.net"
    BNICHOST = "whois.registro.br"
    NORIDHOST = "whois.norid.no"
    IANAHOST = "whois.iana.org"
    PANDIHOST = "whois.pandi.or.id"
    DENICHOST = "de.whois-servers.net"
    AI_HOST = "whois.ai"

    def __init__(self):
        pass

    def get_host(self, website):
        """
        Give a TLD, return the right host to contact

        Args:
            website (str):      website to check

        Returns:
            str:    host to contact to whois the current website
        """
        tld = website.split('.')[-1]
        #  match = re.compile(
        #          'Domain Name: {}\s*.*?Whois Server: (.*?)\s'.format(website), flags=re.IGNORECASE|re.DOTALL).search(buf)

        if (tld == 'org' or tld == 'com' or tld == 'net'):
            return 'whois.internic.net'
        else:
            return 'whois.iana.org'

    def get_whois(self, website, port=43):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = self.get_host(website)
        try:
            sock.connect((host, port))
        except (OSError, socket.gaierror) as err:
            raise OSError
            print(
                    'Bind failed, closing the socket: error {}'
                    .format(err.errno))
            sock.close()

        website = struct.pack('>I', len(website)) + website.encode()
        sock.sendall(website)

        try:
            raw_msg = sock.recv(4)
        except OSError:
            raw_msg = ''

        if not raw_msg:
            return None

        msg_len = struct.unpack('>I', raw_msg)[0]

        data = ''
        while len(data) < msg_len:
            packet = sock.recv(msg_len - len(data))
            print(packet.decode())
            if not packet:
                return None
            data += packet.decode()

        print(data)
        sock.close()

    def whois(self):
        pass

# Get the server allocated to the particular IP through IANA
# Request the data from the right server
