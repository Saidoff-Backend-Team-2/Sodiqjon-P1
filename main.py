import environ
from pathlib import Path

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env('.env')
a = list(env("ALLOWED_HOSTS").split(', '))
# a = env("DEBUG")
print(type(a), a)
