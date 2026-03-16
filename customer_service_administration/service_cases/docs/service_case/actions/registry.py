"""Action registry seed for service_case."""

from __future__ import annotations


DOC_ID = "service_case"
ALLOWED_ACTIONS = ['create', 'assign', 'track', 'confirm', 'close', 'classify', 'escalate', 'record', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['open', 'in_progress', 'resolved'], 'transitions_to': None}, 'assign': {'allowed_in_states': ['open', 'in_progress', 'resolved'], 'transitions_to': 'in_progress'}, 'track': {'allowed_in_states': ['open', 'in_progress', 'resolved'], 'transitions_to': None}, 'confirm': {'allowed_in_states': ['open', 'in_progress', 'resolved'], 'transitions_to': 'closed'}, 'close': {'allowed_in_states': ['open', 'in_progress', 'resolved'], 'transitions_to': 'closed'}, 'classify': {'allowed_in_states': ['open', 'in_progress', 'resolved'], 'transitions_to': None}, 'escalate': {'allowed_in_states': ['open', 'in_progress', 'resolved'], 'transitions_to': None}, 'record': {'allowed_in_states': ['open', 'in_progress', 'resolved'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['open', 'in_progress', 'resolved'], 'transitions_to': 'archived'}}

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
