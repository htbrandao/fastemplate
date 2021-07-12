from fastemplate.config import config


def log_request_entries(log_file='log.log'):
    """
    Retrieves the amount of log entries.

    :param str log_file: name of the log file
    :return: int
    """
    lines = open(file=f'{config.ROOT_DIR}/log.log', mode='r').readlines()
    return len(lines)
