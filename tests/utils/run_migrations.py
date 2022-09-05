from alembic.config import Config as AlembicConfig
from alembic import command


def run_migrations(script_location: str, database_url: str) -> None:
    alembic_cfg = AlembicConfig('alembic.ini')
    alembic_cfg.set_main_option('script_location', script_location)
    command.upgrade(alembic_cfg, 'head', tag=database_url)
