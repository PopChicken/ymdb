"""
this module provides the interfaces of CUD on tag table

"""

from ymdb.models import *
from ymdb.service.exception import ServiceException

from django.db.utils import IntegrityError


def add_tag(req: dict) -> None:
    tag = Tag()
    tag.name = req.get('name')

    try:
        tag.save()
    except IntegrityError:
        return ServiceException("add failed. here might be an existed tag name")


def del_tag(req: dict) -> None:
    tag: Tag = Tag.objects.filter(name=req.get('name')).first()

    if tag is None:
        return ServiceException("tag not exists")
    tag.delete()


def update_tag(req: dict) -> dict:
    tag: Tag = Tag.objects.filter(name=req.get('name'))

    new_name: str = req.get('new_name')
    tag.name = new_name

    try:
        tag.save()
    except IntegrityError:
        return ServiceException("update failed. here might be an existed tag name")


def all_tags() -> dict:
    tags = Tag.objects.all()

    resp = {'tag_list': []}
    tag_list = resp['tag_list']

    for tag in tags:
        tag: Tag
        tag_list.append(tag.name)

    return resp
