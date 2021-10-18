"""
this module provides the interfaces of complex query

"""

from ymdb.models import *
from ymdb.service.exception import ServiceException


def search_manga(req: dict) -> dict:
    title: str = req.get('title')
    tags: list = req.get('tag')
    author: str = req.get('author')
    gallery: str = req.get('gallery')
    minRating: float = req.get('minRating')

    mangas = Manga.objects.all()
    if title is not None:
        mangas = mangas.filter(title__icontains=title)

    if author is not None:
        mangas = mangas.filter(author__icontains=author)

    if minRating is not None:
        mangas = mangas.filter(rating__gte=minRating)
    
    real_tags = Tag.objects
    if tags is not None:
        for tag in tags:
            real_tags = real_tags.filter(name__icontains=tag)
        real_tags = list(real_tags.values_list('tag_id'))

        for tag_id, in real_tags:
            mangas = Manga.objects.filter(tags__tag_id=tag_id)
    
    resp = {'manga_list': []}
    manga_list = resp['manga_list']
    for manga in mangas:
        manga: Manga
        manga_list.append({
            'manga_id': manga.manga_id,
            'title': manga.title,
            'author': manga.author,
            'brief': manga.brief,
            'rating': manga.rating
        })

    return resp


def search_tag(req: dict) -> dict:
    text: str = req['text']
    tags = Tag.objects.filter(name__icontains=text)

    resp = {'tag_list': []}
    tag_list = resp['tag_list']

    for tag in tags:
        tag: Tag
        tag_list.append(tag.name)
    
    return resp


def get_manga_tags(req: dict) -> dict:
    manga_id: int = req['manga_id']
    manga: Manga = Manga.objects.filter(manga_id=manga_id).first()

    if manga is None:
        return ServiceException("manga not exists")
    
    resp = {'tag_list': []}
    tag_list = resp['tag_list']

    for tag in manga.tags.all():
        tag: Tag
        tag_list.append(tag.name)
    
    return resp


def get_gallery_mangas(req: dict) -> dict:
    name: str = req['name']
    gallery: Gallery = Gallery.objects.filter(name=name).first()

    if gallery is None:
        return ServiceException("gallery not exists")
    
    resp = {'manga_list': []}
    manga_list = resp['manga_list']

    for manga in gallery.mangas.all():
        manga: Manga
        manga_list.append({
            'id': manga.manga_id,
            'title': manga.title,
            'author': manga.author,
            'brief': manga.brief,
            'rating': manga.rating
        })

    return resp
