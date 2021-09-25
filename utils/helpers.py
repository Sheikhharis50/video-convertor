from datetime import datetime


def log(message, level='error'):
    now = datetime.now()
    LEVEL_MAP = {
        'error': 'ERROR',
        'warn': 'WARNING',
        'info': 'INFO',
    }
    print(f'[{LEVEL_MAP[level]} | {now.strftime("%m/%d/%Y-%H:%M:%S")}][{message}]')
