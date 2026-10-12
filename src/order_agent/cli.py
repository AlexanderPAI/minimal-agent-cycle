from typing import Dict

from src.order_agent.logging_setup import logger
from src.order_agent.config import config
from src.order_agent.tools import lookup_order, calculate_total

if __name__ == '__main__':
    logger.info("Starting order agent")

    order = lookup_order("ORD-104")

    if not isinstance(order, Dict):
        logger.info(order)
    else:
        logger.info(order)
        total_price = calculate_total([order])
        logger.info(f"Total price: {total_price}")
