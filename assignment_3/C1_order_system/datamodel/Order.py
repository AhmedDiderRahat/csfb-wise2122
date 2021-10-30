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
        #
        # TODO: complete constructor with attributes and initialization
        #
        self.__id = _id                     # private, final attribute, cannot be altered

    #
    # TODO: complete class
    #

class OrderItem:
    def __init__(self, _sku: str, _units: int):
        """
        Constructor
        :param _sku: ordered item (attribute is foreign key in class Stock)
        :param _units: ordered units
        """
        self.__sku = _sku       # private, final attribute, cannot be altered, foreign key in class Stock
        self.units = _units

    def get_sku(self):
        return self.__sku
