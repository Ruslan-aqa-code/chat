from datetime import datetime

import pytest

from domain.entities.messages import Message, Chat
from domain.exceptions.messages import TitleTooLongException
from domain.values.messages import Text, Title


def test_create_message_success_short_text():
    text = Text("Hello World!")
    message = Message(text=text)

    assert message.text == text
    assert message.created_at.date() == datetime.today().date()


def test_create_message_long_text():
    text = Text("a" * 550)
    message = Message(text=text)

    assert message.text == text
    assert message.created_at.date() == datetime.today().date()


def test_create_chat_success():
    title = Title("title")
    chat = Chat(title=title)

    assert chat.title == title
    assert not chat.messages
    assert chat.created_at.date() == datetime.today().date()


def test_create_chat_title_too_long():
    with pytest.raises(TitleTooLongException):
        Title("A" * 500)


def test_message_add_to_chat():
    text = Text("Hello World!")
    message = Message(text=text)

    title = Title("title")
    chat = Chat(title=title)

    chat.add_message(message)

    assert message in chat.messages
