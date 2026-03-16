"""Action handler seed for communication_log_entry:record."""

from __future__ import annotations


DOC_ID = "communication_log_entry"
ACTION_ID = "record"
ACTION_RULE = {'allowed_in_states': ['active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['correspondence_record'], 'borrowed_fields': ['correspondence type', 'subject from correspondence_record'], 'inferred_roles': ['approver']}, 'actors': ['approver'], 'action_actors': {'record': ['approver'], 'archive': ['approver']}}

def handle_record(payload: dict, context: dict | None = None) -> dict:
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
