import logging

LOG_LEVEL = logging.info
LOG_FORMAT = '%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s: %(message)s'



def get_logger(name):
    # define the logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(LOG_FORMAT)

    # file handling
    file_handler = logging.FileHandler('./log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # stream handling
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)


    # add handlers
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger