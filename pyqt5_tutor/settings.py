import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CONFIG_FILE = os.path.join(BASE_DIR, 'config.ini')

LOGGER = (
    {
        'version': 1,
        'formatters': {
            'default': {
                'class': 'logging.Formatter',
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
            },
            'syslog': {
                'class': 'logging.handlers.SysLogHandler',
                'level': 'INFO'
            },
        },
        'loggers': {
            '': {
                'handlers': ['console', 'syslog']
            }
        },
    }
)


"""
    'logfile': {
        'class': 'logging.FileHandler',
        'filename': 'default.log',
        'mode': 'w',
        'formatter': 'default',
    },
    'errors': {
        'class': 'logging.FileHandler',
        'filename': 'default-errors.log',
        'mode': 'w',
        'level': 'ERROR',
        'formatter': 'default',
    },
"""
