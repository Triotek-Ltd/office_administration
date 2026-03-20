"""Action registry seed for schedule_request."""

from __future__ import annotations

from typing import Any


DOC_ID = "schedule_request"
ALLOWED_ACTIONS = ['create', 'review', 'confirm', 'cancel', 'close']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['draft', 'proposed', 'confirmed', 'cancelled'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'proposed', 'confirmed', 'cancelled'], 'transitions_to': None}, 'confirm': {'allowed_in_states': ['draft', 'proposed', 'confirmed', 'cancelled'], 'transitions_to': 'confirmed'}, 'cancel': {'allowed_in_states': ['draft', 'proposed', 'confirmed', 'cancelled'], 'transitions_to': None}, 'close': {'allowed_in_states': ['draft', 'proposed', 'confirmed', 'cancelled'], 'transitions_to': 'closed'}}

STATE_FIELD = 'workflow_state'

def get_action_handler_name(action_id: str) -> str:
    return f"handle_{action_id}"

def get_action_module_path(action_id: str) -> str:
    return f"actions/{action_id}.py"

def action_contract(action_id: str) -> dict:
    return {
        "state_field": STATE_FIELD,
        "rule": ACTION_RULES.get(action_id, {}),
    }
