"""Action registry seed for service_resolution."""

from __future__ import annotations


DOC_ID = "service_resolution"
ALLOWED_ACTIONS = ['create', 'review', 'confirm', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'confirmed'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'confirmed'], 'transitions_to': None}, 'confirm': {'allowed_in_states': ['draft', 'confirmed'], 'transitions_to': 'confirmed'}, 'archive': {'allowed_in_states': ['draft', 'confirmed'], 'transitions_to': 'archived'}}

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
