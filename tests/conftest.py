import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from config.config import get_config
from database.utils.get_sync_engine import get_session_from_engine_connect, get_dev_engine, get_test_engine
from tests.utils.clear_database import clear_database
from tests.utils.run_migrations import run_migrations
from utils.seeding.db_seeder import seed_db

core_config = get_config()


@pytest.fixture(scope="session")
def engine():
    engine = create_async_engine(url=core_config.db_url_test)
    yield engine
    engine.sync_engine.dispose()


@pytest.fixture
async def session(engine):
    yield sessionmaker(
        engine,
        expire_on_commit=False,
        class_=AsyncSession,
    )


@pytest.fixture(scope="session", autouse=True)
def before_tests():
    engine = get_test_engine()
    session = get_session_from_engine_connect(engine)

    clear_database(session=session, engine=engine)

    run_migrations('migrations', core_config.db_url_test)

    with engine.connect() as sql_engine:
        seed_db(session)
