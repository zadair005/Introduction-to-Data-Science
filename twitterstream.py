# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 20:41:29 2018

@author: zadai
"""

import requests
import requests_oauthlib import OAuth1
import jsonlines

api_key = "hZupQjaJu89liEgoS3y3tvC3j"
api_secret = "qS65prwMUygYSjOsIWsMu4mvALP1ClGD73Jet7r1vDqloPfDvN"
access_token = "893618839-t9BK0ziFkQoEaVs3s6ISjS387sGNMYzkEtBaW6SN"
access_token_secret = "RxmBcDqyvBqolOZoslHYRkDTBY5LK2APXb3fUbRkpbTrI"

url - 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(api_key, api_secret, access_token, access_token_secret)

r = requests.get(url, auth=auth)
print(r.status_code)

url = 'https://stream.twitter.com/1.1/statuses/sample.json'
r = requests.get(url, auth=auth, stream=True)
if r.encoding is None:
    r.encoding = 'utf-8'
    
with jsonlines.open('output.json', mode='w') as writer:
    try:
        for line in r.iter_lines(decode_unicode=True):
            if line:
        pass
    