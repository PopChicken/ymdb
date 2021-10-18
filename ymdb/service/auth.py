"""
this module provides the interfaces of jwt

"""

from re import L
import time
import json
import base64
import binascii
import hashlib

from urllib.parse import urlparse

from json.decoder import JSONDecodeError

from Crypto.Cipher import AES

from ymdb.service.exception import AuthException

from ymdb_site.settings import REQ_KEY, REQ_EXPIRE_IN, AUTH_KEY


gen_schema = {
    'type': 'object'
}


def req_encrypt(payload: dict) -> str:
    payload = {
        'exp': round(time.time()) + REQ_EXPIRE_IN,
        'res': payload
    }
    data = json.dumps(payload)
    bs = AES.block_size
    def pad(s): return s + (bs - len(s) % bs) * chr(0)
    cipher = AES.new(REQ_KEY.encode('ascii'), AES.MODE_ECB)
    data = cipher.encrypt(pad(data).encode('utf-8'))
    return base64.urlsafe_b64encode(data).decode('ascii')


def req_decrypt(token: str) -> dict:
    cipher = AES.new(REQ_KEY.encode('ascii'), AES.MODE_ECB)
    try:
        result = base64.urlsafe_b64decode(token)
        data = cipher.decrypt(result)

        data = data.decode('utf-8', 'ignore')
        data = data.rstrip('\n')
        data = data.rstrip('\t')
        data = data.rstrip('\r')
        data = data.replace('\x00','')
        payload: dict = json.loads(data)
    except binascii.Error:
        raise AuthException("bad cipher")
    except ValueError:
        raise AuthException("bad cipher")
    except JSONDecodeError:
        raise AuthException("bad cipher")
    
    exp = payload.get('exp')
    res = payload.get('res')
    if exp is None or res is None:
        raise AuthException("bad plain json")
    if exp < time.time():
        raise AuthException("expired")

    return res


def authenticate_url(url: str) -> str:
    if url is None or url == '':
        return url

    u = urlparse(url)
    path = u.path

    cryptor = hashlib.md5()
    timestamp = hex(round(time.time()))[2:]
    cryptor.update((AUTH_KEY + path + timestamp).encode('ascii'))
    md5hash = cryptor.hexdigest()

    query = f'sign={md5hash}&t={timestamp}'
    if len(u.query) > 0:
        query += '&'
    u = u._replace(query=query + u.query)
    return u.geturl()
