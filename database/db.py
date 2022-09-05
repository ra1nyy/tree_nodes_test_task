from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.pool import NullPool

from config.config import get_config

config = get_config()


class AsyncDb(object):
    def __init__(self, db_url: str, debug: bool):
        engine = create_async_engine(
            db_url,
            echo=debug,
            poolclass=NullPool,
        )

        self.session = sessionmaker(
            engine,
            expire_on_commit=False,
            class_=AsyncSession,
        )


async_db = AsyncDb(
    db_url=config.db_url,
    debug=False,
)


def get_async_db():
    return async_db
