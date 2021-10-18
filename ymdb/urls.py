"""gcp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import ymdb.controller.basic.gallery as gallery
import ymdb.controller.basic.manga as manga
import ymdb.controller.basic.tag as tag
import ymdb.controller.query as query
import ymdb.controller.relate as relate
import ymdb.controller.test as test
import ymdb.controller.auth as auth

from django.urls import path


urlpatterns = [
    path('test', test.ymdb_test),
    path('token/gen', auth.gen_token),
    path('manga/add', manga.add_manga),
    path('manga/del', manga.del_manga),
    path('manga/update', manga.update_manga),
    path('manga/get', manga.get_manga),
    path('manga/setThumbnail', manga.set_thumbnail),
    path('tag/add', tag.add_tag),
    path('tag/del', tag.del_tag),
    path('tag/update', tag.update_tag),
    path('tag/all', tag.all_tags),
    path('gallery/add', gallery.add_gallery),
    path('gallery/del', gallery.del_gallery),
    path('gallery/update', gallery.update_gallery),
    path('manga/search', query.search_manga),
    path('manga/tags', query.get_manga_tags),
    path('tag/search', query.search_tag),
    path('gallery/mangas', query.get_gallery_mangas),
    path('manga/setTag', relate.set_tag),
    path('gallery/addManga', relate.add_to_gallery)
]
