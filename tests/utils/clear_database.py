from sqlalchemy import inspect


def clear_database(session, engine):
    tables = _get_tables(engine)
    with session:
        for table_name in tables:
            session.execute('DROP TABLE IF EXISTS "{0}" CASCADE'.format(table_name))
        session.commit()


def _get_tables(engine) -> list[str]:
    tables: list[str] = []
    inspector = inspect(engine)
    for table_name in inspector.get_table_names(schema='public'):
        tables.append(table_name)

    return tables
