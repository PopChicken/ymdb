"""
this module provides the interfaces of jwt

"""

import ymdb.service.auth as auth
import ymdb.service.util.validate as validator

from ymdb.service.util.resp import success

from django.http.request import HttpRequest
from django.http.response import JsonResponse


gen_schema = {
    'type': 'object'
}


def gen_token(http_req: HttpRequest) -> JsonResponse:
    stat, res = validator.validate(http_req, gen_schema)
    if stat == validator.FAIL:
        return JsonResponse(res)

    token = auth.req_encrypt(res)
    resp = {'token': token}

    return JsonResponse(success(resp))
