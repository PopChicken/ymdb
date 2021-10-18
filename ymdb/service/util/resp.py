def fail(msg: str) -> dict:
    resp = {
        'code': 1,
        'msg': msg,
        'response': None
    }
    return resp


def success(resp_body: dict=None) -> dict:
    resp = {
        'code': 0,
        'msg': "success",
        'response': resp_body
    }
    return resp


