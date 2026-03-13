"""Action handler seed for service_log_entry:view."""

from __future__ import annotations


DOC_ID = "service_log_entry"
ACTION_ID = "view"
ACTION_RULE = {'allowed_in_states': 'active', 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Maintain an auditable history of actions and notes taken during service-case handling.', 'actors': ['service desk officer', 'assigned owner', 'supervisor'], 'start_condition': 'A service case requires action or note capture.', 'ordered_steps': ['Record the service activity against the case.', 'Capture actor, action, and note details.', 'Retain the log entry for audit and case history.'], 'primary_actions': ['record', 'view', 'archive'], 'primary_transitions': ['service_log_entry: active -> archived'], 'downstream_effects': ['Case activity becomes traceable and reviewable.']}

def handle_view(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = ACTION_RULE.get("transitions_to")
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
