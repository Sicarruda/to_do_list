from asyncio.log import logger
import logging

logger = logging.getLogger('app')


def password_validation(password):
    if len(password) < 6:
        logger.error(f'{password} menor de 6 caracteres')
        raise ValueError(f"senha menor que 6 caracteres")
    if len(password) > 20:
        logger.error(f'{password} maior de 20 caracteres')
        raise ValueError(f'senha maior que 20 caracteres')
     