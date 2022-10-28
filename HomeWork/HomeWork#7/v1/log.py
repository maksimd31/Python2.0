import logging

logging.basicConfig(
    level=logging.INFO, filename='telephone_directory.log',
    format='[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s: %(lineno)d] => %(message)s',
    datefmt='%d.%m.%Y %H:%M:%S', encoding='utf-8')
