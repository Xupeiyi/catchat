from datetime import datetime

from sqlalchemy import Table, MetaData, Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, registry

from catchat.model import Message, User


metadata = MetaData()
mapper_registry = registry(metadata=metadata)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("email", String(254), unique=True, nullable=False),
)

message = Table(
    "message",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("body", Text, nullable=False),
    Column("timestamp", DateTime, default=datetime.utcnow, index=True),
    Column("author_id", Integer, ForeignKey("user.id"))
)


def start_mappers():
    message_mapper = mapper_registry.map_imperatively(
        Message,
        message,
        properties={
            'author': relationship(User)
        }
    )
    mapper_registry.map_imperatively(
        User,
        user,
        properties={
            "messages": relationship(
                message_mapper, collection_class=set
            )
        }
    )
