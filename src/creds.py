import os


def get_secret_key():
    SECRET_KEY = str(os.getenv("SECRET_KEY", None))
    return SECRET_KEY


def get_owner_id():
    OWNER_ID = str(os.getenv("OWNER_ID", "495662327711137797"))
    return int(OWNER_ID)
