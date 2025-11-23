from .base import *

DEBUG = False

ALLOWED_HOSTS = [ 
        os.getenv("ALLOWED_HOST", "127.0.0.1")
]