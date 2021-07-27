from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from fastemplate import logger

router = APIRouter()

templates = Jinja2Templates(directory='docs/_build/html')


@router.get("/index.html", response_class=HTMLResponse, include_in_schema=False)
def index():
    """
    Returns api's documentation HTML files.

    :return: HTML
    """
    logger.info('Request@/index.html')
    return templates.get_template("index.html").render()
