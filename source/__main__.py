import uvicorn

from configuration import SETTINGS

uvicorn.run(
    app='service:app',
    host='0.0.0.0',
    port=SETTINGS.HTTP_PORT,
    access_log=False,
)
