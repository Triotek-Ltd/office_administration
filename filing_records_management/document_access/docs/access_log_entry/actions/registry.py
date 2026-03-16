"""Action registry seed for access_log_entry."""

from __future__ import annotations


DOC_ID = "access_log_entry"
ALLOWED_ACTIONS = ['record', 'view', 'archive']
ACTION_RULES = {'record': {'allowed_in_states': ['active'], 'transitions_to': None}, 'view': {'allowed_in_states': ['active'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['active'], 'transitions_to': 'archived'}}

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
