import asyncio

from core.tree_traverse_cte import get_nodes_after_traverse
from database.db import get_async_db


def main():
    async_db = get_async_db()
    nodes = asyncio.run(
        get_nodes_after_traverse(
            session=async_db.session,
            depth=6,
        )
    )

    for node in nodes:
        print(node)
    print(f"TOTAL: {len(nodes)}")


if __name__ == "__main__":
    main()
