from sqlalchemy import select, literal, desc
from sqlalchemy.ext.asyncio import AsyncSession

from config.config import get_config
from database import NodeEntity
from models import Node


async def tree_traverse_cte(
    session: AsyncSession,
    sort_field: str = 'title',
    sort_dir: str = 'asc',
    depth: int = 1,
    start_node: str = None
) -> list[Node] | None:
    if not start_node:
        start_node = get_config().root_node_title

    tree = select(NodeEntity, literal(0).label('level')).filter(
        NodeEntity.title == start_node
    ).cte(name='tree', recursive=True)

    tree = tree.union_all(
        select(NodeEntity, (tree.c.level + 1).label('level')).filter(
            NodeEntity.parent_id == tree.c.id,
            tree.c.level + 1 <= depth,
        )
    )

    order_by = desc(sort_field) if sort_dir == 'desc' else sort_field
    result_nodes = await session.scalars(
        select(NodeEntity).join(tree, NodeEntity.id == tree.c.id).order_by(order_by)
    )

    return Node.get_models_from_query(result_nodes)


async def get_nodes_after_traverse(
    session: AsyncSession,
    sort_field: str = 'title',
    sort_dir: str = 'asc',
    depth: int = 1,
    start_node: str = None
) -> list[Node] | None:
    async with session() as session:
        return await tree_traverse_cte(
            session=session,
            sort_field=sort_field,
            sort_dir=sort_dir,
            depth=depth,
            start_node=start_node,
        )
