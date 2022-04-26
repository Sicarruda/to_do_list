from asyncio.log import logger
import re
import logging


logger = logging.getLogger('app')


def email_validation(email):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

    if match == None:
        logger.error(f'{email} não tem a forma correta')
        raise ValueError(f'{email} não tem a forma correta')

