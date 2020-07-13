import pytest

from todo_list import ToDoListBase


@pytest.fixture
def todo_instance():
    instance = ToDoListBase()
    instance.add_item("qwerty")
    return instance


def test__add_item(todo_instance):
    todo_instance.add_item("apples")
    assert "apples" in todo_instance.categories["unspecified"]

def test_add_item():
    assert False


def test_remove_item_by_value():
    assert False


def test_remove_item_by_index():
    assert False


def test_display_list():
    assert False
