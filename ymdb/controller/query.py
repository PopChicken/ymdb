"""
this module provides the interfaces of complex query

"""
import ymdb.service.util.validate as validator
import ymdb.service.data.query as data

from ymdb.service.exception import ServiceException
from ymdb.service.util.resp import success, fail

from django.http.request import HttpRequest
from django.http.response import JsonResponse

from ymdb.models import *


manga_schema = {
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

tag_schema = {
    'type': 'object',
    'required': ['text'],
    'properties': {
        'text': {'type': 'string', 'minLength': 1}
    }
}

manga_tags_schema = {
    'type': 'object',
    'required': ['manga_id'],
    'properties': {
        'manga_id': {'type': 'integer', 'minimum': 1}
    }
}

gallery_mangas_schema = {
    'type': 'object',
    'required': ['name'],
    'properties': {
        'name': {'type': 'string', 'maxLength': 38, 'minLength': 2},
    }
}


def search_manga(http_req: HttpRequest) -> JsonResponse:
    stat, res = validator.validate(http_req, manga_schema)
    if stat == validator.FAIL:
        return JsonResponse(res)

    try:
        resp = data.search_manga(res)
    except ServiceException as e:
        return JsonResponse(fail(e.msg))

    return JsonResponse(success(resp))


def search_tag(http_req: HttpRequest) -> JsonResponse:
    stat, res = validator.validate(http_req, tag_schema)
    if stat == validator.FAIL:
        return JsonResponse(res)

    try:
        resp = data.search_tag(res)
    except ServiceException as e:
        return JsonResponse(fail(e.msg))

    return JsonResponse(success(resp))


def get_manga_tags(http_req: HttpRequest) -> JsonResponse:
    stat, res = validator.validate(http_req, manga_tags_schema)
    if stat == validator.FAIL:
        return JsonResponse(res)
    
    try:
        resp = data.get_manga_tags(res)
    except ServiceException as e:
        return JsonResponse(fail(e.msg))

    return JsonResponse(success(resp))


def get_gallery_mangas(http_req: HttpRequest) -> JsonResponse:
    stat, res = validator.validate(http_req, gallery_mangas_schema)
    if stat == validator.FAIL:
        return JsonResponse(res)
    
    try:
        resp = data.get_gallery_mangas(res)
    except ServiceException as e:
        return JsonResponse(fail(e.msg))

    return JsonResponse(success(resp))
