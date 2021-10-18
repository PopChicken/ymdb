"""
this module provides the interfaces of CRUD on manga table

"""

from ymdb.models import *
from ymdb.service.exception import ServiceException

from django.db.utils import IntegrityError


def add_manga(req: dict) -> dict:
    manga = Manga()
    manga.title = req.get('title')
    manga.author = req.get('author')
    manga.brief = req.get('brief')
    manga.rating = req.get('rating')

    try:
        manga.save()
    except IntegrityError:
        return ServiceException("add failed. here might be an existed title")

    return {
        'manga_id': manga.manga_id
    }


def del_manga(req: dict) -> None:
    manga: Manga = Manga.objects.filter(manga_id=req.get('manga_id')).first()

    if manga is None:
        raise ServiceException("manga not exists")
    
    manga.delete()


def update_manga(req: dict) -> None:
    manga: Manga = Manga.objects.get(manga_id=req.get('manga_id'))
    
    title = req.get('title')
    author = req.get('author')
    brief = req.get('brief')
    rating = req.get('rating')

    if title is not None:
        manga.title = title
    if author is not None:
        manga.author = author
    if brief is not None:
        manga.brief = brief
    if rating is not None:
        manga.rating = rating

    try:
        manga.save()
    except IntegrityError:
        return ServiceException("add failed. here might be an existed title")


def get_manga(req: dict) -> dict:
    manga_id = req['manga_id']
    manga: Manga = Manga.objects.filter(manga_id=manga_id).first()
    
    if manga is None:
        raise ServiceException("manga not exists")
    
    tag_list = []
    for tag in manga.tags.all():
        tag: Tag
        tag_list.append(tag.name)
    
    resp = {
        'id': manga.manga_id,
        'title': manga.title,
        'thumbnail': manga.thumbnail,
        'thumbnail_id': manga.thumbnail_id,
        'author': manga.author,
        'brief': manga.brief,
        'rating': manga.rating,
        'tags': tag_list
    }

    return resp


def set_thumbnail(req: dict) -> None:
    manga_id = req['manga_id']
    thumbnail = req['thumbnail']
    thumbnail_id = req['thumbnail_id']
    manga: Manga = Manga.objects.filter(manga_id=manga_id).first()

    if manga is None:
        return ServiceException("manga not exists")
    
    manga.thumbnail = thumbnail
    manga.thumbnail_id = thumbnail_id

    try:
        manga.save()
    except IntegrityError:
        return ServiceException("illegal thumbnail url")
