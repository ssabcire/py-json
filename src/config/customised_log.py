from logging import LogRecord

import json_log_formatter


class CustomisedJSONFormatter(json_log_formatter.JSONFormatter):
    def json_record(self, message: str, extra: dict, record: LogRecord) -> dict:
        '''log output to JSON format
        https://github.com/marselester/json-log-formatter
        '''
        # https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry
        extra['message'] = message
        extra['severity'] = record.levelname

        extra['logger_name'] = record.name
        extra['module'] = record.module

        if record.exc_info:
            extra['exc_info'] = self.formatException(record.exc_info)

        return extra
