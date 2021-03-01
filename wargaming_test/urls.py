from aiohttp import web

from . import views

routes = [
    web.get('/fibonachi', views.get_fibonacci),
]
