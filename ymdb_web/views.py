import jsonschema

import ymdb.service.auth as auth
import ymdb.service.data.basic.manga as manga
import ymdb.service.data.query as query

from jsonschema.exceptions import ValidationError

from ymdb.service.exception import AuthException
from ymdb.controller.basic.manga import get_schema as detail_schema
from ymdb.controller.query import manga_schema as search_schema

from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseNotFound


def detail(http_req: HttpRequest, token: str) -> HttpResponse:
    try:
        req = auth.req_decrypt(token)
        jsonschema.validate(req, detail_schema)
    except AuthException:
        return HttpResponseNotFound()
    except ValidationError:
        return HttpResponseNotFound()

    context = manga.get_manga(req)
    context['thumbnail'] = auth.authenticate_url(context['thumbnail'])
    return render(http_req, 'ymdb_web/detail.html', context)


def search(http_req: HttpRequest, token: str) -> HttpResponse:
    try:
        req = auth.req_decrypt(token)
        jsonschema.validate(req, search_schema)
    except AuthException:
        return HttpResponseNotFound()
    except ValidationError:
        return HttpResponseNotFound()

    context = query.search_manga(req)
    manga_list = context['manga_list']

    for manga in manga_list:
        token = auth.req_encrypt({
            'manga_id': manga['manga_id']
        })
        manga['link'] = f'/manga/detail/{token}'
        manga['thumbnail'] = auth.authenticate_url(manga['thumbnail'])

    return render(http_req, 'ymdb_web/result.html', context)
