from abstract_storage import AbstractStorage
from exceptions import NotEnoughSpase, NotEnoughProduct, UnknownProduct


class BaseStorage(AbstractStorage):
    def __init__(self, items, capacity):
        self.__items = items
        self.__capacity = capacity

    def add(self, name, count):
        if self.get_free_space() < count:
            raise NotEnoughSpase
        if name in self.__items:
            self.__items[name] += count
        else:
            self.__items[name] = count

    def remove(self, name, count):
        if name not in self.__items:
            raise UnknownProduct
        if self.__items[name] < count:
            raise NotEnoughProduct

        self.__items[name] -= count
        if self.__items[name] == 0:
            del self.__items[name]

    def get_free_space(self):
        return self.__capacity - sum(self.__items.values())

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items.keys())

