from C1_order_system.datamodel import Order


class OrderDataStore:
    """
    class that defines a container to hold Order objects and
    provide functions to access, filter and query data
    """

    def __init__(self):
        """
        Constructor
        """
        self.__data = {}

    def add_order(self, _order: Order):
        self.__data[_order.get_id()] = _order

    def remove_order(self, _order_id: int):
        self.__data.pop(_order_id, None)  # remove key from dict, return object if key existed or None otherwise

    def size(self) -> int:
        return len(self.__data)

    def find_all_orders(self) -> []:
        return list(self.__data.values())

    def find_order_by_id(self, _id: str) -> Order:
        return self.__data.get(_id)  # get(key) returns None if key is not found

    def filter(self, _filter_func: bool) -> [Order]:
        _filtered = []
        for c in self.__data.values():
            if _filter_func(c):
                _filtered.append(c)
        return _filtered
