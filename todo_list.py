#!/bin/python3
from typing import TYPE_CHECKING
from loguru import logger

if TYPE_CHECKING:
    from typing import List, Optional, Dict, Tuple


class ToDoListBase:
    def __init__(self):
        # self.list_items: List[str] = []
        self.categories: Dict[str, List[str]] = {"work": [], "shopping": [], "unspecified": []}

    def _add_item(self, item: str, category: str = "unspecified"):
        self.categories[category].append(item)
        # logger.debug(f"This is a log")

    def add_item(self, item: str, category: str = "unspecified"):
        try:
            self._add_item(item, category)

        except KeyError:
            self.categories[category] = []
            self._add_item(item, category)
        # self.list_items.append(item)

    def is_item_in_categories(self, item: str):
        # -> Tuple[bool, str]
        # Loop over all categories
        # Loop over items in each category
        # Check if the item of interest is present in any of the available categories and their respective items
        raise NotImplementedError

    def _remove_item_by_value(self, item: str, category: str = "unspecified"):
        try:
            try:
                self.categories[category].remove(item)

            except ValueError:
                print("Sorry your item does not exist in the list to remove it")

        except KeyError:
            print("Sorry your category does not exist")

    def remove_item_by_value(self, item: str, category: str = "unspecified"):
        # self.list_items.remove(item_value)
        self._remove_item_by_value(item, category)

    # def remove_item_by_index(self, item_index: int, category: str = "unspecified"):
    #     try:
    #         # self.list_items.pop(item_index)
    #         self.categories[category].pop(item_index)
    #
    #     except IndexError:
    #         print("Sorry your index is out of range. Nothing was removed")
    #
    # def display_list(self):
    #     # print(self.list_items)


if __name__ == '__main__':
    a = ToDoListBase()
    a.add_item("this is a test")
    a.add_item("qwerty", "work")
    # a.display_list()
    # a.remove_item_by_index(4)
    # a.display_list()
    a.remove_item_by_value("qwerty")

