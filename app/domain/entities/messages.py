from dataclasses import dataclass, field
from domain.entities.base import BaseEntity
from domain.values.messages import Text, Title


@dataclass
class Message(BaseEntity):
    __hash__ = BaseEntity.__hash__

    text: Text


@dataclass
class Chat(BaseEntity):
    __hash__ = BaseEntity.__hash__

    title: Title
    messages: set[Message] = field(
        default_factory=set,
        kw_only=True,
    )

    def add_message(self, message: Message) -> None:
        self.messages.add(message)
