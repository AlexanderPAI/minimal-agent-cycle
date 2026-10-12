from typing import Any, Dict

from src.order_agent.logging_setup import logger
from src.order_agent.config import config
from src.order_agent.tools import dispatch


if __name__ == '__main__':
    logger.info("Starting order agent")

    action = "lookup_order"
    arguments =  {"order_id": "ORD-101"}

    order = dispatch(action, arguments)
    logger.info(order)

    action = "calculate_total"
    arguments = {"order": order.data}

    result = dispatch(action, arguments)

    logger.info(result)
