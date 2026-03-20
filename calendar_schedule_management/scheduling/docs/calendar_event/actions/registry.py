"""Action registry seed for calendar_event."""

from __future__ import annotations

from typing import Any


DOC_ID = "calendar_event"
ALLOWED_ACTIONS = ['create', 'update', 'confirm', 'cancel', 'archive']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['scheduled', 'completed', 'cancelled'], 'transitions_to': None}, 'update': {'allowed_in_states': ['scheduled', 'completed', 'cancelled'], 'transitions_to': None}, 'confirm': {'allowed_in_states': ['scheduled', 'completed', 'cancelled'], 'transitions_to': 'completed'}, 'cancel': {'allowed_in_states': ['scheduled', 'completed', 'cancelled'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['scheduled', 'completed', 'cancelled'], 'transitions_to': 'archived'}}

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
