"""
this module provides the interfaces of CRUD on manga table

"""

import ymdb.service.util.validate as validator
import ymdb.service.data.basic.manga as data

from ymdb.service.exception import ServiceException
from ymdb.service.util.resp import success, fail

from django.http.request import HttpRequest
from django.http.response import JsonResponse

from ymdb.models import *


add_schema = {
    'type': 'object',
    'required': ['title', 'author', 'brief', 'rating'],
    'properties': {
        'title': {'type': 'string', 'maxLength': 64, 'minLength': 4},
        'author': {'type': 'string', 'maxLength': 38, 'minLength': 2},
        'brief': {'type': 'string'},
        'rating': {'type': 'number', 'minimum': 0, 'maximum': 10}
    }
}

del_schema = {
    'type': 'object',
    'required': ['manga_id'],
    'properties': {
        'manga_id': {'type': 'integer', 'minimum': 1}
    }
}

update_schema = {
    'type': 'object',
    'required': ['manga_id'],
    'properties': {
        'manga_id': {'type': 'integer', 'minimum': 1},
        'title': {'type': 'string', 'maxLength': 38, 'minLength': 4},
        'author': {'type': 'string', 'maxLength': 38, 'minLength': 2},
        'brief': {'type': 'string'},
        'rating': {'type': 'number', 'minimum': 0, 'maximum': 10}
    }
}

get_schema = {
    'type': 'object',
    'required': ['manga_id'],
    'properties': {
        'manga_id': {'type': 'integer', 'minimum': 1}
    }
}

thumbnail_schema = {
    'type': 'object',
    'required': ['manga_id'],
    'properties': {
        'manga_id': {'type': 'integer', 'minimum': 1},
        'thumbnail_id': {'type': 'integer', 'minimum': 1},
        'thumbnail': {'type': 'string', 'format': 'uri', "pattern": "^https?://"}
    }
}


def add_manga(http_req: HttpRequest) -> JsonResponse:
    stat, res = validator.validate(http_req, add_schema)
    if stat == validator.FAIL:
        return JsonResponse(res)

    try:
        resp = data.add_manga(res)
    except ServiceException as e:
        return JsonResponse(fail(e.msg))

    return JsonResponse(success(resp))


def del_manga(http_req: HttpRequest) -> JsonResponse:
    stat, res = validator.validate(http_req, del_schema)
    if stat == validator.FAIL:
        return JsonResponse(res)
    
    try:
        resp = data.del_manga(res)
    except ServiceException as e:
        return JsonResponse(fail(e.msg))

    return JsonResponse(success(resp))


def update_manga(http_req: HttpRequest) -> JsonResponse:
    stat, res = validator.validate(http_req, update_schema)
    if stat == validator.FAIL:
        return JsonResponse(res)
    
    try:
        resp = data.update_manga(res)
    except ServiceException as e:
        return JsonResponse(fail(e.msg))

    return JsonResponse(success(resp))


def get_manga(http_req: HttpRequest) -> JsonResponse:
    stat, res = validator.validate(http_req, get_schema)
    if stat == validator.FAIL:
        return JsonResponse(res)

    try:
        resp = data.get_manga(res)
    except ServiceException as e:
        return JsonResponse(fail(e.msg))

    return JsonResponse(success(resp))


def set_thumbnail(http_req: HttpRequest) -> JsonResponse:
    stat, res = validator.validate(http_req, thumbnail_schema)
    if stat == validator.FAIL:
        return JsonResponse(res)
    
    try:
        resp = data.set_thumbnail(res)
    except ServiceException as e:
        return JsonResponse(fail(e.msg))

    return JsonResponse(success(resp))
