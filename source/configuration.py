__all__ = ['SETTINGS', 'LOGGER']

from logging import Formatter
from logging import getLogger
from logging import StreamHandler
import sys

from pydantic import BaseSettings
from pydantic import Field
from pydantic import ValidationError

formatter = Formatter('| %(levelname)s | %(name)s | %(asctime)s | %(message)s', datefmt='%d/%m/%y %H:%M:%S')
to_console = StreamHandler()
to_console.setFormatter(formatter)
LOGGER = getLogger('challenge')
LOGGER.addHandler(to_console)
LOGGER.setLevel('DEBUG')


class _Settings(BaseSettings):
    HTTP_PORT: int = Field(
        default=8080,
        description='Porta HTTP em que será disponibilizada a API REST'
    )


try:
    SETTINGS = _Settings()
except ValidationError:
    LOGGER.critical('🚨 Alguma variável de ambiente não foi definida. Confira na documentação.')
    sys.exit(1)
