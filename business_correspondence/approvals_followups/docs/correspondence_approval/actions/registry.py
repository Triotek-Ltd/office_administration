"""Action registry seed for correspondence_approval."""

from __future__ import annotations


DOC_ID = "correspondence_approval"
ALLOWED_ACTIONS = ['submit', 'approve', 'return_for_revision', 'close']
ACTION_RULES = {'submit': {'allowed_in_states': ['open', 'in_review', 'approved'], 'transitions_to': 'in_review'}, 'approve': {'allowed_in_states': ['open', 'in_review', 'approved'], 'transitions_to': 'approved'}, 'return_for_revision': {'allowed_in_states': ['open', 'in_review', 'approved'], 'transitions_to': None}, 'close': {'allowed_in_states': ['open', 'in_review', 'approved'], 'transitions_to': 'closed'}}

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
