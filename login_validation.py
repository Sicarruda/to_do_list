from asyncio.log import logger
import logging
from flask import Flask, request



logger = logging.getLogger('app')

def login_validation(id_user):
    cookie = request.cookies.get('userID')
    if cookie == None:
        logger.error(f'cookie inexistente')
        raise ValueError(f'cookie inexistente')
    elif cookie != id_user:
        logger.error(f'cookie incorreto')
        raise ValueError(f'cookie incorreto')
    else:
        return
