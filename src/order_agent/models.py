from typing import Dict, List, Literal, Optional
from pydantic import BaseModel, Field


class AgentState(BaseModel):
    """Agent state."""
    run_id: str = Field(..., description="ID of running agent process")
    goal: str = Field(..., description="Goal of agent. Question of user")
    status: Literal["running", "success", "failed", "needs_input"] = Field(..., description="Status of agent")
    step_count: int = Field(..., description="Step count of agent")
    max_steps: int = Field(..., description="Max number of steps of agent")
    facts: Dict[str, object] = Field({}, description="Dictionary of collected facts")
    history: List[Dict[str, object]] = Field([], description="History of agent")
    final_answer: Optional[str] = Field(None, description="Final answer of agent")
    error: Optional[str] = Field(None, description="Error message of agent")


class ActionDecision(BaseModel):
    """Action decision."""
    action: Literal["lookup_order", "calculate_total", "finish", "ask_user"] = Field(..., description="Title of Action")
    arguments: Dict[str, object] = Field({}, description="Dictionary of arguments for Action")
    reason: str = Field(..., description="Reason of action decision")


class ToolResult(BaseModel):
    """Tool result."""
    ok: bool = Field(..., description="Whether tool was successful")
    data: Dict[str, object] = Field({}, description="Data of tool result")
    code_error: Optional[int] = Field(None, description="Error code of tool")
    error: Optional[str] = Field(None, description="Error message of tool")


class StepRecord(BaseModel):
    """Step record."""
    step_count: int = Field(..., description="Step count of agent")
    action: ActionDecision = Field(..., description="Action decision of agent")
    arguments: Dict[str, object] = Field({}, description="Dictionary of valid arguments for Action")
    tool_result: ToolResult = Field(..., description="Tool result of tool")
    transition: str = Field(..., description="Transition of AgentState status")
    reason: str = Field(..., description="Reason of action decision")
    duration: int = Field(..., description="Duration of action decision")
    total_tokens: int = Field(..., description="Total number of tokens of LLM")
