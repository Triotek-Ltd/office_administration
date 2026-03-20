"""Action registry seed for administrative_document."""

from __future__ import annotations

from typing import Any


DOC_ID = "administrative_document"
ALLOWED_ACTIONS = ['create', 'update', 'review', 'archive', 'classify', 'file', 'register']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['draft', 'active', 'disposed'], 'transitions_to': None}, 'update': {'allowed_in_states': ['draft', 'active', 'disposed'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'active', 'disposed'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'active', 'disposed'], 'transitions_to': 'archived'}, 'classify': {'allowed_in_states': ['draft', 'active', 'disposed'], 'transitions_to': None}, 'file': {'allowed_in_states': ['draft', 'active', 'disposed'], 'transitions_to': None}, 'register': {'allowed_in_states': ['draft', 'active', 'disposed'], 'transitions_to': None}}

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
