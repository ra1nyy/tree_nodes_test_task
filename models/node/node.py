import uuid
from datetime import datetime
from models.modelBase import ModelBase


class Node(ModelBase):
    id: uuid.UUID = None

    parent_id: uuid.UUID | None

    title: str | None

    #registered_in: datetime = None
