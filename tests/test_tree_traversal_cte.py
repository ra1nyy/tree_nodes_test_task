import pytest

from core.tree_traverse_cte import get_nodes_after_traverse


@pytest.mark.asyncio
async def test_count_of_nodes(session):
    # [(depth, count_of_nodes)]
    expected_values = [(0, 1), (1, 6), (2, 31), (3, 156), (4, 781)]

    for value in expected_values:
        nodes = await get_nodes_after_traverse(
            session=session,
            depth=value[0],
        )
        assert len(nodes) == value[1]


async def test_traversal_sorted_by_id_desc():
    pass


async def test_traversal_sorted_by_id_asc():
    pass


async def test_traversal_sorted_by_field():
    pass


async def test_traversal_from_random_node():
    pass
