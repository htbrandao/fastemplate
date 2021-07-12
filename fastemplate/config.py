import os


class Config:
    """
    Class to include variables related to the application.
    """
    ROOT_DIR = "/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1])


config = Config()
