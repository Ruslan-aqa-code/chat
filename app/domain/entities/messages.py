from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from domain.values.messages import Text, Title


@dataclass
class Message:
    oid: str = field(
        default_factory=lambda: str(uuid4()),
        kw_only=True,
    )
    text: Text
    created_at: datetime = field(
        default_factory=datetime.now,
        kw_only=True,
    )


@dataclass
class Chat:
    oid: str = field(
        default_factory=lambda: str(uuid4()),
        kw_only=True,
    )
    title: Title
    messages: set[Message] = field(
        default_factory=set,
        kw_only=True,
    )
