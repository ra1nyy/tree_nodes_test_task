from sqlalchemy.orm import Session

from config.config import get_config
from database.utils.get_sync_engine import get_dev_engine, get_session_from_engine_connect
from utils.seeding.count_of_data import NODES_DEPTH, COUNT_OF_CHILDREN
from utils.seeding.nodes.add_nodes import add_nodes


def seed_db(sql_session: Session):
    app_cfg = get_config()

    print('--- start seeding ---')
    add_nodes(
        depth=NODES_DEPTH,
        count_of_children=COUNT_OF_CHILDREN,
        session=sql_session,
        root_node_title=app_cfg.root_node_title,
    )
    sql_session.commit()
    print('--- finish ---')


if __name__ == '__main__':
    engine = get_dev_engine()
    with engine.connect() as sql_engine:
        session = get_session_from_engine_connect(sql_engine)
        seed_db(session)
