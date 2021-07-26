import os

class Config:
    """
    Class to include variables related to the application.
    """
    ROOT_DIR = "/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1])
    NAME = 'FASTEMPLATE'
    DESCRIPTION = 'REST API Template to ease your understanding!'
    ALLOW_CORS = True
    SECURE_API = False

config = Config()
