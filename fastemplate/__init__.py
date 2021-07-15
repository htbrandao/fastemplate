__version__ = '0.0.1'
__api_version__ = 'v1'

from loguru import logger
from fastapi import FastAPI
from datetime import datetime
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from fastemplate.config import config
from fastemplate.services.v1 import v1
from fastemplate.services import docs, metrics
from fastemplate.exceptions.handler import exceptions_handler

NAME = 'FASTEMPLATE'
DESCRIPTION = 'REST API Template to ease your understanding!'

ALLOW_CORS = False

logger.add('fastemplate.log', rotation='5 MB')

app = FastAPI(
    title='FasTemplate',
    description=DESCRIPTION,
    version=__version__,
    # docs_url=f'/{__api_version__}/docs',
    # redoc_url=f'/{__api_version__}/redoc'
)


@app.get('/')
def root():
    """
    Root endpoint.

    :return: dict: basic api info
    """
    logger.info('Request @ /')
    timestamp = datetime.now().strftime('%d-%m-%YT%H:%M:%S')
    return {
        'APPLICATION': NAME,
        'VERSION': f'{__version__}',
        'API VERSION': __api_version__,
        'DOCUMENTATION': '/index.html',
        '@TIMESTAMP': timestamp,
    }


app.include_router(v1, prefix=f'/{__api_version__}')

app.include_router(metrics.router)

app.include_router(docs.router)
app.mount('/pages', StaticFiles(directory='docs/_build/html/pages'), name='pages')
app.mount('/_static', StaticFiles(directory='docs/_build/html/_static'), name='static')
app.mount('/_modules', StaticFiles(directory='docs/_build/html/_modules'), name='modules')

exceptions_handler(app=app)

if ALLOW_CORS:
    app.add_middleware(CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True
    )
