from fastapi import APIRouter

router = APIRouter()


@router.get('/hello_world')
async def hello_world():
    return 'Hello World, Olá Mundo, Hola Mundo, ...'
