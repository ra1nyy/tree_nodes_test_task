from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config.config import get_config

config = get_config()
engine = create_engine(config.db_url.replace('+asyncpg', ''))
engine_for_tests = create_engine(config.db_url_test.replace('+asyncpg', ''))


def get_dev_engine():
    return engine


def get_test_engine():
    return engine_for_tests


def get_session_from_engine_connect(sql_engine_connect):
    return Session(bind=sql_engine_connect)
