import json
from datetime import datetime, timedelta
from json import JSONDecodeError
from typing import Any, Dict

from openrouter import OpenRouter

from src.order_agent.config import config
from src.order_agent.models import ActionDecision, AgentState


class Model:
    """Model"""

    def __init__(self) -> None:
        self.model = OpenRouter(
            api_key=config.openrouter_api_key,
            timeout_ms=config.llm_timeout_ms,
        )
        self.model_ref = config.openrouter_model

    def invoke(self, system_prompt: Dict[str, Any], user_prompt: Dict[str, Any]):
        """Invoke the model."""
        with self.model:
            response = self.model.chat.send(
                model=self.model_ref,
                messages=[system_prompt, user_prompt],
                response_format={
                    "type": "json_schema",
                    "json_schema": {
                        "name": "action_decision",
                        "strict": True,
                        "schema": ActionDecision.model_json_schema()
                    }
                }
            )
            return json.loads(response.choices[0].message.content)
