import os


def get_secret_key():
    SECRET_KEY = str(os.getenv("SECRET_KEY", None))
    return SECRET_KEY
