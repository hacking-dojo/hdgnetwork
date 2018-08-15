# -*- coding: utf-8 -*-
import requests
import json

BASE_URL = 'https://rdap.arin.net/registry/ip/'


class Whois():

    def __init__(self):
        pass

    def get_from_ip(self, ip_str):

        rdap_url_request = BASE_URL + str(ip_str)
        req = requests.get(rdap_url_request)
        output = json.loads(req.text)

        if 'entities' not in output:
            return None

        first_vcard = output['entities'][0]['vcardArray'][1]
        owner = ''
        addr = ''

        for block in first_vcard:
            if block[0] == 'fn':
                owner = block[3]
            if block[0] == 'adr':
                addr = block[1]['label']

        answer = dict()
        answer["owner"] = owner
        answer["addr"] = addr
        json_answer = json.dumps(answer)
        return json_answer
