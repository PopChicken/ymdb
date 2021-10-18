import base64
import json
import time
import binascii
import jsonschema

from Crypto.Cipher import AES

from json.decoder import JSONDecodeError


REQ_KEY = 'rM253rF7CGy6tV8J'


def req_encrypt(payload: dict) -> str:
    payload = {
        'exp': round(time.time()) + 300,
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
        raise Exception("bad cipher")
    except ValueError:
        raise Exception("bad cipher")
    except JSONDecodeError:
        raise Exception("bad cipher")
    
    exp = payload.get('exp')
    res = payload.get('res')
    if exp is None or res is None:
        raise Exception("bad plain json")
    if exp == time.time():
        raise Exception("expired")

    return res


search_schema = {
    'type': 'object',
    'required': [],
    'properties': {
        'title': {'type': 'string'},
        'tag': {
            'type': 'array',
            'items': {
                'type': 'string',
                'minLength': 1
            }
        },
        'author': {'type': 'string', 'minLength': 1},
        'gallery': {'type': 'string', 'minLength': 1},
        'minRating': {'type': 'number', 'minimum': 0, 'maximum': 10}
    }
}

token = req_encrypt({"aaaaa": 123124312})
print(token)
payload = req_decrypt(token)
print(payload)
jsonschema.validate(payload, search_schema)