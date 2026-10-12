from typing import Dict, List


FAKE_ORDERS = {
    "ORD-101": {"items": {"item1": {"price": 1200}, "item2": {"price": 800}}, "delivery_price": 300},
    "ORD-102": {"items": {"item1": {"price": 450}}, "delivery_price": 0},
    "ORD-103": {"items": {"item1": {"price": 150}, "item2": {"price": 250}, "item3": {"price": 400}}, "delivery_price": 200}
}


def lookup_order(order_id: str) -> Dict | str:
    """Get information about an order by ID."""
    pass


def calculate_total(orders: List[Dict[str, object]]) -> int:
    """Calculate the total price of an order and delivery price."""
    pass
