"""Action registry seed for records_register_entry."""

from __future__ import annotations


DOC_ID = "records_register_entry"
ALLOWED_ACTIONS = ['create', 'record', 'review', 'archive', 'view']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'active'], 'transitions_to': None}, 'record': {'allowed_in_states': ['draft', 'active'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'active'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'active'], 'transitions_to': 'archived'}, 'view': {'allowed_in_states': ['draft', 'active'], 'transitions_to': None}}

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
