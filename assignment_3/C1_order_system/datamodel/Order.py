from datetime import datetime


class Order:
    """
    class that defines an Order entity, which represents a transaction
    between a selling business and a Customer
    """

    def __init__(self, _id: str, _customer_id: int, _date: datetime = datetime.now()):
        """
        Constructor
        :param _id: order id attribute (private, final, cannot be altered)
        :param _customer_id: reference to owning customer (attribute is foreign key in class Customer)
        :param _date: date order was placed (default value is 'now')
        """
        self.__id = _id  # private, final attribute, cannot be altered
        self.__customer_id = _customer_id
        self.__date = _date
        self.__items = []

    def get_id(self) -> str:
        """
        id getter, returns private customer identifier
        :return: customer identifier
        """
        return self.__id

    def get_customer_id(self) -> int:
        """
        return the customer id of any order
        """

        return self.__customer_id

    def get_date(self) -> datetime:
        """
        return the datetime of an order
        """

        return self.__date

    def add_item(self, _sku: str, _units: int) -> int:
        """
        add item to the order
        """
        _item = OrderItem(_sku, _units)
        self.__items.append(_item)
        return self.items_count()

    def items_count(self) -> int:
        """
        returns the counter of an items
        """
        return len(self.__items)

    def get_item(self, _i: int) -> object:
        """
        returns the i-th element of the list
        """
        return self.__items[_i] if 0 <= _i < len(self.__items) else None

class OrderItem:
    def __init__(self, _sku: str, _units: int):
        """
        Constructor
        :param _sku: ordered item (attribute is foreign key in class Stock)
        :param _units: ordered units
        """
        self.__sku = _sku  # private, final attribute, cannot be altered, foreign key in class Stock
        self.units = _units

    def get_sku(self):
        return self.__sku
