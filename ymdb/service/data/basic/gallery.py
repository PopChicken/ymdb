"""
this module provides the interfaces of CUD on gallery table

"""

from ymdb.models import *
from ymdb.service.exception import ServiceException

from django.db.utils import IntegrityError


def add_gallery(req: dict) -> None:
    gallery = Gallery()
    gallery.name = req.get('name')
    gallery.owner = req.get('owner')
    gallery.description = req.get('description')

    try:
        gallery.save()
    except IntegrityError:
        raise ServiceException(
            "add failed. here might be an existed gallery name")


def del_gallery(req: dict) -> None:
    gallery: Gallery = Gallery.objects.filter(tag_id=req.get('name')).first()

    if gallery is None:
        raise ServiceException("gallery not exists")
    
    gallery.delete()


def update_gallery(req: dict) -> None:
    gallery: Gallery = Gallery.objects.filter(name=req.get('name')).first()

    if gallery is None:
        raise ServiceException("gallery not exists")

    new_name: str = req.get('new_name')
    owner: str = req.get('owner')
    description: str = req.get('description')

    if new_name is not None:
        gallery.name = new_name
    if owner is not None:
        gallery.owner = owner
    if description is not None:
        gallery.description = description

    try:
        gallery.save()
    except IntegrityError:
        raise ServiceException("update failed. here might be an existed tag name")
