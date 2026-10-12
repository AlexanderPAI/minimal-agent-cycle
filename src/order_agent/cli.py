from src.order_agent.logging_setup import logger
from src.order_agent.tools import dispatch
from src.order_agent.agent import Model
from src.order_agent.prompts import DECISION_SYSTEM_PROMPT


model = Model()


if __name__ == '__main__':
    logger.info("Starting order agent")

    system_prompt = {
        "role": "system",
        "content": DECISION_SYSTEM_PROMPT
    }

    user_prompt = {
        "role": "user",
        "content": "Какова итоговая стоимость заказа ORD-101 с доставкой?"
    }

    result = model.invoke(system_prompt, user_prompt)

    print(type(result))
