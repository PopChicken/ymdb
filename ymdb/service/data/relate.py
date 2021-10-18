"""
this module provides the interfaces to build relations

"""
from ymdb.models import *
from ymdb.service.exception import ServiceException


def set_tag(req: dict) -> None:
    manga_id: int = req['manga_id']
    tag_name: str = req['tag']
    manga: Manga = Manga.objects.filter(manga_id=manga_id).first()
    tag: Tag = Tag.objects.filter(name=tag_name).first()

    if tag is None:
        return ServiceException("tag not exists")
    if manga is None:
        return ServiceException("manga not exists")
    
    try:
        manga.tags.add(tag)
    except:
        return ServiceException("fail to add tag to manga")


def add_to_gallery(req: dict) -> None:
    gallery_name: str = req['gallery']
    manga_id: int = req['manga_id']
    gallery: Gallery = Gallery.objects.filter(name=gallery_name).first()
    manga: Manga = Manga.objects.filter(manga_id=manga_id).first()

    if gallery is None:
        return ServiceException("gallery not exists")
    if manga is None:
        return ServiceException("manga not exists")
    
    try:
        gallery.mangas.add(manga)
    except:
        return ServiceException("fail to add manga to gallery")
