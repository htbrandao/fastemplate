__version__ = '0.0.1'
__api_version__ = 'v1'

from datetime import datetime

from loguru import logger
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles

from fastemplate.config import config
from fastemplate.services.v1 import v1
from fastemplate.services.utils import allow_cors
from fastemplate.services import docs, metrics, login
from fastemplate.exceptions.handler import exceptions_handler

logger.add('fastemplate.log', rotation='5 MB')

app = FastAPI(
    title='FasTemplate',
    description=config.DESCRIPTION,
    version=__version__
)

if config.ALLOW_CORS:
    allow_cors(app=app)


@app.get('/')
def root():
    """
    Root endpoint.

    :return: dict: basic api info
    """
    logger.info('Request@/')
    timestamp = datetime.now().strftime('%d-%m-%YT%H:%M:%S')
    return {
        'APPLICATION': config.NAME,
        'VERSION': f'{__version__}',
        'API VERSION': __api_version__,
        'DOCUMENTATION': '/index.html',
        '@TIMESTAMP': timestamp,
    }


app.include_router(metrics.router)
app.include_router(login.router, prefix='/login', tags=['login'])
app.include_router(v1, prefix=f'/{__api_version__}')

app.include_router(docs.router, tags=['docs'])
app.mount('/pages', StaticFiles(directory='docs/_build/html/pages'), name='pages')
app.mount('/_static', StaticFiles(directory='docs/_build/html/_static'), name='static')
app.mount('/_modules', StaticFiles(directory='docs/_build/html/_modules'), name='modules')

exceptions_handler(app=app)
