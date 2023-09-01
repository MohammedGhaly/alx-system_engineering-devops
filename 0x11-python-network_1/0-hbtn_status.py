#!/usr/bin/python3
'''a script that fetches https://alx-intranet.hbtn.io/status'''


import urllib.request as uq


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    req = uq.Request(url)
    with uq.urlopen(req) as response:
        res = response.read()
        print('Body response:')
        print(f'\t- type: {type(res)}')
        print(f'\t- content: {res}')
        print(f'\t- utf8 content: {res.decode("utf8")}')
