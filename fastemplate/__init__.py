__version__ = '0.0.1'
__api_version__ = 'v1'

from loguru import logger
from fastapi import FastAPI
from datetime import datetime
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from fastemplate.config import config
from fastemplate.services import docs, metrics
from fastemplate.services.v1 import v1
from fastemplate.exceptions.handler import exceptions_handler

NAME = 'FASTEMPLATE'
DESCRIPTION = 'REST API Template to ease your understanding!'

logger.add('log.log', rotation='500 MB')

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
app.mount('/pages', StaticFiles(directory=f'{config.ROOT_DIR}/docs/_build/html/pages'), name='pages')
app.mount('/_static', StaticFiles(directory=f'{config.ROOT_DIR}/docs/_build/html/_static'), name='static')
app.mount('/_sources', StaticFiles(directory=f'{config.ROOT_DIR}/docs/_build/html/_sources'), name='sources')
app.mount('/_images', StaticFiles(directory=f'{config.ROOT_DIR}/docs/_build/html/_static'), name='images')

exceptions_handler(app)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_credentials=True,
#     allow_headers=["*"]
# )
