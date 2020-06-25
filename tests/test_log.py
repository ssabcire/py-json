import json
from logging import config, getLogger

from config.log_config import LOGGER


def test_log(capsys):
    config.dictConfig(LOGGER)
    logger = getLogger('zeals')
    logger.warning('occur error')
    expected = json.dumps({
        "message": "occur error",
        "severity": "WARNING",
        "logger_name": "zeals",
        "module": "test_log",
    }) + "\n"
    out, err = capsys.readouterr()
    assert out == expected
    assert err == ''
