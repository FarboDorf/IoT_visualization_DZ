import math


def truck_loads(orders):
    if (not isinstance(orders, (int))):
        return None
    if (orders <= 0):
        return [0]

    trucks = math.ceil(orders / 40)
    load_per_truck = orders // trucks
    remaining_orders = orders % trucks
    loads = [load_per_truck + 1] * remaining_orders + [load_per_truck] * (trucks - remaining_orders)
    return loads
