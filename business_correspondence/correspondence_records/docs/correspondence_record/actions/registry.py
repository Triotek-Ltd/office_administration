"""Action registry seed for correspondence_record."""

from __future__ import annotations


DOC_ID = "correspondence_record"
ALLOWED_ACTIONS = ['create', 'review', 'submit', 'approve', 'return_for_revision', 'issue', 'send', 'file', 'track', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'in_review', 'approved', 'sent'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'in_review', 'approved', 'sent'], 'transitions_to': 'in_review'}, 'submit': {'allowed_in_states': ['draft', 'in_review', 'approved', 'sent'], 'transitions_to': 'in_review'}, 'approve': {'allowed_in_states': ['draft', 'in_review', 'approved', 'sent'], 'transitions_to': 'approved'}, 'return_for_revision': {'allowed_in_states': ['draft', 'in_review', 'approved', 'sent'], 'transitions_to': None}, 'issue': {'allowed_in_states': ['draft', 'in_review', 'approved', 'sent'], 'transitions_to': None}, 'send': {'allowed_in_states': ['draft', 'in_review', 'approved', 'sent'], 'transitions_to': None}, 'file': {'allowed_in_states': ['draft', 'in_review', 'approved', 'sent'], 'transitions_to': None}, 'track': {'allowed_in_states': ['draft', 'in_review', 'approved', 'sent'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'in_review', 'approved', 'sent'], 'transitions_to': 'archived'}}

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
