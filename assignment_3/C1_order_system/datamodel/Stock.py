class Stock:
    """
    class that defines a Stock entity, which can be ordered
    """

    def __init__(self, _id: str, _description: str = "", _price: int = 0, _units_available: int = 0):
        """
        Constructor
        :param _id: stock keeping unit (SKU) attribute (private, final, cannot be altered)
        :param _description: description of article or stock unit
        :param _price: price (private, in cent)
        :param _units_available: units available in stock (private)
        """
        self.__sku = _id  # private, final, cannot be altered
        self.description = _description
        self.__price = _price
        self.__unit_available = _units_available

    def get_sku(self) -> str:
        """
        id getter, returns private stock identifier
        :return: stock identifier
        """
        return self.__sku

    def get_price(self) -> int:
        """
        price getter return price of a stock item
        """
        return self.__price

    def set_price(self, _price):
        """
        set the price of a stock item
        """
        self.__price = _price

    def get_unit_available(self) -> int:
        """
        get the available unit of any product
        """
        return self.__unit_available

    def has_units_available(self, _n: int) -> bool:
        """has any unit available for this stocked item"""
        return self.get_unit_available() >= _n

    def transact_units(self, _n: int) -> bool:

        """
        this function made the transaction of any item

        if _n is negative then the item count will decrease otherwise vice-versa
        """

        if _n >= 0:
            # for adding case
            self.unit_available += _n
            return True
        else:
            # for any item removing case
            if self.has_units_available(_n):
                self.unit_available -= _n
                return True

        return False
