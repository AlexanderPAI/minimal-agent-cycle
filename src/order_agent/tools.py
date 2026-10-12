from typing import Any, Dict, List


FAKE_ORDERS = {
    "ORD-101": {"items": {"item1": {"price": 1200}, "item2": {"price": 800}}, "delivery_price": 300},
    "ORD-102": {"items": {"item1": {"price": 450}}, "delivery_price": 0},
    "ORD-103": {"items": {"item1": {"price": 150}, "item2": {"price": 250}, "item3": {"price": 400}}, "delivery_price": 200}
}


def lookup_order(order_id: str) -> Dict | str:
    """Get information about an order by ID."""
    return FAKE_ORDERS.get(order_id, "order_not_found")


def calculate_total(orders: List[Dict[str, Any]]) -> int:
    """Calculate the total price of an order and delivery price."""
    total_price = 0

    for order in orders:
        total_price += order["delivery_price"]
        if isinstance(order["items"], Dict):
            for item in order["items"].values():
                total_price += item["price"]

    return total_price
