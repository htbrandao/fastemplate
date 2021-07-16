from fastemplate.config import config


def log_request_entries(log_file='fastemplate.log'):
    """
    Retrieves the amount of log entries.

    :param str log_file: name of the log file
    :return: int
    """
    lines = open(file=log_file, mode='r').readlines()
    return len(lines)
