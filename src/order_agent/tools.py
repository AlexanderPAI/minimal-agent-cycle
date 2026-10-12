from typing import Any, Dict, List

from src.order_agent.models import ToolResult


FAKE_ORDERS = {
    "ORD-101": {"items": {"item1": {"price": 1200}, "item2": {"price": 800}}, "delivery_price": 300},
    "ORD-102": {"items": {"item1": {"price": 450}}, "delivery_price": 0},
    "ORD-103": {"items": {"item1": {"price": 150}, "item2": {"price": 250}, "item3": {"price": 400}}, "delivery_price": 200}
}



def lookup_order(order_id: str) -> ToolResult:
    """Get information about an order by ID."""
    db_result = FAKE_ORDERS.get(order_id, "order_not_found")
    if not isinstance(db_result, Dict):
        return ToolResult(
            ok=False,
            error=db_result,
        )

    return ToolResult(
        ok=True,
        data=db_result,
    )


def calculate_total(orders: List[Dict[str, Any]]) -> ToolResult:
    """Calculate the total price of an order and delivery price."""
    total_price = 0

    for order in orders:
        total_price += order["delivery_price"]
        if isinstance(order["items"], Dict):
            for item in order["items"].values():
                total_price += item["price"]

    return ToolResult(
        ok=True,
        data={"total_price": total_price},
    )


TOOL_REGISTRY = {
    "lookup_order": lookup_order,
    "calculate_total": calculate_total,
}


def dispatch(action: str, arguments: Dict[str, Any]) -> ToolResult:
    """Dispatch action to tool registry"""
    tool = TOOL_REGISTRY.get(action)
    if tool is None:
        return ToolResult(ok=False, error="Unknown action")
    return tool(arguments)