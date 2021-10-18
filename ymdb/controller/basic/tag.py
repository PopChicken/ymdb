"""
this module provides the interfaces of CUD on tag table

"""
import ymdb.service.util.validate as validator
import ymdb.service.data.basic.tag as data

from ymdb.service.exception import ServiceException
from ymdb.service.util.resp import success, fail

from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.db.utils import IntegrityError

from ymdb.models import *


add_schema = {
    'type': 'object',
    'required': ['name'],
    'properties': {
        'name': {'type': 'string', 'maxLength': 38, 'minLength': 2}
    }
}

del_schema = {
    'type': 'object',
    'required': ['name'],
    'properties': {
        'name': {'type': 'string', 'maxLength': 38, 'minLength': 2}
    }
}

update_schema = {
    'type': 'object',
    'required': ['name', 'new_name'],
    'properties': {
        'name': {'type': 'string', 'maxLength': 38, 'minLength': 2},
        'new_name': {'type': 'string', 'maxLength': 38, 'minLength': 2}
    }
}


def add_tag(http_req: HttpRequest) -> JsonResponse:
    stat, res = validator.validate(http_req, add_schema)
    if stat == validator.FAIL:
        return JsonResponse(res)

    try:
        resp = data.add_tag(res)
    except ServiceException as e:
        return JsonResponse(fail(e.msg))

    return JsonResponse(success(resp))


def del_tag(http_req: HttpRequest) -> JsonResponse:
    stat, res = validator.validate(http_req, del_schema)
    if stat == validator.FAIL:
        return JsonResponse(res)
    
    try:
        resp = data.del_tag(res)
    except ServiceException as e:
        return JsonResponse(fail(e.msg))

    return JsonResponse(success(resp))


def update_tag(http_req: HttpRequest) -> JsonResponse:
    stat, res = validator.validate(http_req, update_schema)
    if stat == validator.FAIL:
        return JsonResponse(res)
    
    try:
        resp = data.update_tag(res)
    except ServiceException as e:
        return JsonResponse(fail(e.msg))

    return JsonResponse(success(resp))


def all_tags(_: HttpRequest) -> JsonResponse:
    try:
        resp = data.all_tags()
    except ServiceException as e:
        return JsonResponse(fail(e.msg))

    return JsonResponse(success(resp))
