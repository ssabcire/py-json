from logging import config, getLogger

from flask import Flask

from config.log_config import LOGGER

app = Flask(__name__)


@app.route('/')
def hello():
    config.dictConfig(LOGGER)
    logger = getLogger('zeals')
    logger.info('test\n I want to eat sushi', {"id": 1234, "name": "tamaki"})
    try:
        raise ValueError('something wrong')
    except ValueError:
        logger.exception(f'Request failed.', exc_info=True)

    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
