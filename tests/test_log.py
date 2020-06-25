import json
from logging import config, getLogger

from config.config import LOGGER


def test_log(capsys):
    config.dictConfig(LOGGER)
    logger = getLogger('zeals')
    logger.info('test')
    expected = json.dumps({
        "message": "occur error",
        "severity": "WARNING",
        "logger_name": "saturn",
        "module": "test_log",
    }) + "\n"
    out, err = capsys.readouterr()
    assert out == expected
    assert err == ''
