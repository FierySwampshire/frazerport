from datetime import datetime

formatsExplaination = {
    't': 'short time',
    'T': 'long time',
    'd': 'short date',
    'D': 'long date',
    'f': 'short date time',
    'F': 'long date time',
    "R": 'relative time',
}


def timestamp():
    return int(datetime.now().timestamp())


time_tag_builder = '<{t}:{timestamp}:{style}>'.format
