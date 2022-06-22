from os import walk
from os.path import dirname, join
from os.path import realpath
from runpy import run_path

from fastapi import APIRouter
from fastapi import FastAPI

from configuration import LOGGER

app = FastAPI(
    title='Mario Guedes | Desafio técnico do processo seletivo para a 4intelligence | 1735396 - Backend Developer (Remote)',
    version='0.1.0',
)

directory_api_rest = join(dirname(realpath(__file__)), 'rest')
for root, dirs, files in walk(directory_api_rest):
    for file in files:
        if file.endswith('.py'):
            module = join(root, file)

            LOGGER.debug('Carregando o módulo: %s', module)

            buffer = run_path(module)
            for _, value in buffer.items():
                if isinstance(value, APIRouter):
                    app.include_router(value)