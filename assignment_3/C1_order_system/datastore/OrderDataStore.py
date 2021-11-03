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

    #
    # TODO: complete missing functions
    #

    def add_order(self, _order: Order):
        self.__data[_order.get_id()] = _order

    def size(self) -> int:
        return len(self.__data)

    def find_all_orders(self) -> []:
        #
        # TODO: complete function
        #
        return []

    def filter(self, _filter_func: bool) -> [Order]:
        #
        # TODO: complete function
        #
        return []
