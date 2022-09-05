from dotenv import dotenv_values
from os.path import exists
import os


def load_config(env_file='.env'):
    if exists(env_file):
        return load_from_file(env_file)

    return load_from_env()


def load_from_file(env_file):
    return dotenv_values(env_file)


def load_from_env():
    return os.environ
