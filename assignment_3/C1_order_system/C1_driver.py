import sys

sys.path.append("..")  # Path hack needed to run from commandline
from C1_order_system.datamodel import Order, last_name_func
from C1_order_system import cds, sds, ods

"""
Customer, Stock, Order, OrderItem are classes defined in the datamodel module.
Objects of these classes are business objects relevant for order processing.

cds, sds, ods are global singleton objects defined the C1_order_system_full module
(C1_order_system_full.__init__.py):
 - cds, data store with Customer objects (subjects in orders)
 - sds, data store with Stock objects (orderable items)
 - ods, data store with Order objects (represent orders with >= 1 ordered items)
"""


def print_order_items(o: Order) -> int:
    """
    Print value of an order by compounding all ordered items.
    :param o: order object
    :return: total value of order in cent
    """
    print(f"- order {o.get_id()} ({o.items_count()} item):")
    _order_value = 0

    for _item_index in range(o.items_count()):
        _item = o.get_item(_item_index)

        _stock_sku = _item.get_sku()
        _stock_units = _item.units

        _stock = sds.find_stock_by_id(_stock_sku)
        _stock_price = _stock.get_price()
        _stock_description = _stock.description
        _stock_total_price = _stock_units * _stock_price

        _order_value += _stock_total_price

        print(f"  - {_stock_units} x {_stock_description} = {float(_stock_total_price)}")

    print(f"  --> order value is: {float(_order_value)}")

    return _order_value


def print_orders(_customer_id: int):
    """
    Print all orders of a customer and compounding their total value
    that is printed at the end.
    :param _customer_id: customer id
    """

    # 193667 986973
    # _customer_id = 986973

    _total_price = 0

    _customer_orders = ods.filter(lambda o: o.get_customer_id() == _customer_id)

    print(f"\n--> customer {_customer_id} has {len(_customer_orders)} orders")

    for _order in _customer_orders:
        _total_price += print_order_items(_order)

    print(f"==> total order value is: {float(_total_price)}")


if __name__ == "__main__":
    # print number of orders in OrderStore and CustomerStore
    print(f"{len(ods.find_all_orders())} orders in OrderStore")
    print(f"{len(cds.find_all_customers())} customers in CustomerStore")

    # find customers in data store using find functions
    _c1 = cds.find_customer_by_id(898179)
    print("customer 898179:", _c1.name if _c1 is not None else "not found")

    # find customers using filter functions on data stores
    _last_name = "Cantrell"
    print(f"--> find customers with last name '{_last_name}':")
    _filtered_by_id = cds.filter(lambda c: c.get_id() == 898179 or c.get_id() == 192794)
    _filtered_by_name = cds.filter(lambda c: last_name_func(c) == _last_name)
    # print resulting customer list using the built-in map() function
    list(map(lambda c: print(f" - {c.name}, {c.address}"), _filtered_by_name))

    # Look up for one stock item
    _stock_id = "1718C002"
    _s1 = sds.find_stock_by_id(_stock_id)
    print("\nLook up stock and order data\n")
    print(f"--->Find Information of Stock ID '{_stock_id}': ")
    print(f"Price= {_s1.get_price()} and Unit available ={_s1.get_unit_available()}\n")

    _order_id = "00-784-33313"
    _ord1 = ods.find_order_by_id(_order_id)
    print(f"--->Find Information of Order ID '{_order_id}': ")
    print(f"Customer Id= {_ord1.get_customer_id()}, Order Date ={_ord1.get_date()}, "
          f"Total Item: {_ord1.items_count()}\n")

    # find all orders for each customer
    print_orders(258090)  # customer 258090: 2 orders with 1 item each
    print_orders(368075)    # customer 368075: 1 order with 1 item each
    print_orders(986973)    # customer 986973: 1 order with 4 items
    print_orders(193667)    # customer 193667: 4 orders with 1 item each
    print_orders(973407)    # customer 973407: 0 orders, is customer
    print_orders(333333)    # customer 333333: 0 orders, not a customer
    print_orders(-1)        # customer -1: illegal customer id
