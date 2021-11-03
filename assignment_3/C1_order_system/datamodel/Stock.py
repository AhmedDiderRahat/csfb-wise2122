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
        self.__sku = _id                            # private, final, cannot be altered
        self.description = _description
        self.price = _price
        self.unit_available = _units_available

    def get_id(self) -> int:
        """
        id getter, returns private customer identifier
        :return: customer identifier
        """
        return self.__sku
