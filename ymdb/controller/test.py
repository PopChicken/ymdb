"""
this module provides the interfaces of test

"""
from django.http.request import HttpRequest
from django.http.response import JsonResponse


def ymdb_test(_: HttpRequest) -> JsonResponse:
    return JsonResponse({
        'code': 0
    })
