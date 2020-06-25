from logging import config, getLogger

from flask import Flask

from config.log_config import LOGGER


app = Flask(__name__)


@app.route('/')
def hello():
    config.dictConfig(LOGGER)
    logger = getLogger('zeals')
    logger.info('test')
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
