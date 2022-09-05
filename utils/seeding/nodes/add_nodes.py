import random
import string
import uuid

from sqlalchemy.orm import Session

from database import NodeEntity
from models import Node


def get_node(parent_id: uuid.UUID = None, title: str = None) -> Node:
    return Node(
        id=uuid.uuid4(),
        parent_id=parent_id,
        title=title if title else ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
    )


def get_child_nodes(parent_id: uuid.UUID, count_of_children: int) -> list[Node]:
    return [get_node(parent_id) for _ in range(count_of_children)]


def get_tree(depth: int, count_of_children: int, root_node_title: str = 'root') -> list[Node] | None:
    if depth - 1 <= 0:
        return None

    start_node = get_node(title=root_node_title)
    tree_nodes = [start_node]
    roots = [start_node]
    for i in range(depth - 1):
        future_roots = []
        for root in roots:
            children = get_child_nodes(root.id, count_of_children)
            tree_nodes.extend(children)
            future_roots.extend(children)
        roots = future_roots
    return tree_nodes


def add_nodes(depth: int, count_of_children: int, session: Session, root_node_title: str = 'root'):
    tree_of_nodes = get_tree(depth, count_of_children, root_node_title)
    session.bulk_save_objects([NodeEntity.from_model(node) for node in tree_of_nodes])
    session.flush()
