LOGGER = {
    'version': 1,
    'formatters': {
        'default': {
            '()': 'config.customised_log.CustomisedJSONFormatter'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'default',
            'stream': 'ext://sys.stdout'
        },
    },
    'loggers': {
        'zeals': {
            'level': 'DEBUG',
            'handlers': ['console']
        }
    }
}