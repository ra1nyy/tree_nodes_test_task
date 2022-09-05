import uuid

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

from database.base import Base
from database.entityBase import EntityBase
from models import Node


class NodeEntity(Base, EntityBase[Node]):
    __tablename__ = 'nodes'
    update_ignore_fields = {'id', 'registered_in'}
    model = Node

    id = sa.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    parent_id = sa.Column(
        'parent_id',
        UUID(as_uuid=True),
        sa.ForeignKey('nodes.id'),
        index=True,
        nullable=True,
    )

    title = sa.Column('title', sa.VARCHAR, nullable=True)

    registered_in = sa.Column(
        'created_at',
        sa.TIMESTAMP(True),
        nullable=False,
        server_default=sa.func.now(),
    )
