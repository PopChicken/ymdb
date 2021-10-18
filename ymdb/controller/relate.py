"""
this module provides the interfaces to build relations

"""
import ymdb.service.util.validate as validator

from ymdb.service.util.resp import success, fail

from django.http.request import HttpRequest
from django.http.response import JsonResponse

from ymdb.models import *


set_tag_schema = {
    'type': 'object',
    'required': ['manga_id', 'tag'],
    'properties': {
        'manga_id': {'type': 'integer', 'minimum': 1},
        'tag': {'type': 'string', 'minLength': 2, 'maxLength': 38}
    }
}

add_to_gallery_schema = {
    'type': 'object',
    'required': ['gallery', 'manga_id'],
    'properties': {
        'gallery': {'type': 'string', 'maxLength': 38, 'minLength': 2},
        'manga_id': {'type': 'integer', 'minimum': 1}
    }
}


def set_tag(http_req: HttpRequest) -> JsonResponse:
    stat, res = validator.validate(http_req, set_tag_schema)
    if stat == validator.FAIL:
        return JsonResponse(res)

    manga_id: int = res['manga_id']
    tag_name: str = res['tag']
    manga: Manga = Manga.objects.filter(manga_id=manga_id).first()
    tag: Tag = Tag.objects.filter(name=tag_name).first()

    if tag is None:
        return JsonResponse(fail("tag not exists"))
    if manga is None:
        return JsonResponse(fail("manga not exists"))
    
    try:
        manga.tags.add(tag)
    except:
        return JsonResponse(fail("fail to add tag to manga"))

    return JsonResponse(success())


def add_to_gallery(http_req: HttpRequest) -> JsonResponse:
    stat, res = validator.validate(http_req, add_to_gallery_schema)
    if stat == validator.FAIL:
        return JsonResponse(res)
    
    gallery_name: str = res['gallery']
    manga_id: int = res['manga_id']
    gallery: Gallery = Gallery.objects.filter(name=gallery_name).first()
    manga: Manga = Manga.objects.filter(manga_id=manga_id).first()

    if gallery is None:
        return JsonResponse(fail("gallery not exists"))
    if manga is None:
        return JsonResponse(fail("manga not exists"))
    
    try:
        gallery.mangas.add(manga)
    except:
        return JsonResponse(fail("fail to add manga to gallery"))

    return JsonResponse(success())
