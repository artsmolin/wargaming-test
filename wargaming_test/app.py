from aiohttp import web
from loguru import logger

from wargaming_test import urls


def get_web_app() -> web.Application:
    app = web.Application()
    app.add_routes(urls.routes)
    return app


if __name__ == "__main__":
    logger.info('Run app')
    web_app = get_web_app()
    web.run_app(web_app)
