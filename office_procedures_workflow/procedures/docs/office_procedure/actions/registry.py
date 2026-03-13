"""Action registry seed for office_procedure."""

from __future__ import annotations


DOC_ID = "office_procedure"
ALLOWED_ACTIONS = ['create', 'update', 'review', 'publish', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': None}, 'update': {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': None}, 'publish': {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': 'published'}, 'archive': {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': 'archived'}}

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
