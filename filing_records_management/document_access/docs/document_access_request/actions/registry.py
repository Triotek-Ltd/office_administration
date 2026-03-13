"""Action registry seed for document_access_request."""

from __future__ import annotations


DOC_ID = "document_access_request"
ALLOWED_ACTIONS = ['create', 'assign', 'approve', 'close']
ACTION_RULES = {'create': {'allowed_in_states': ['open', 'in_review', 'resolved'], 'transitions_to': None}, 'assign': {'allowed_in_states': ['open', 'in_review', 'resolved'], 'transitions_to': 'in_review'}, 'approve': {'allowed_in_states': ['open', 'in_review', 'resolved'], 'transitions_to': None}, 'close': {'allowed_in_states': ['open', 'in_review', 'resolved'], 'transitions_to': 'closed'}}

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
