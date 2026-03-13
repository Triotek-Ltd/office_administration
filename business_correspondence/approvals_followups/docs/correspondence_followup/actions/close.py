"""Action handler seed for correspondence_followup:close."""

from __future__ import annotations


DOC_ID = "correspondence_followup"
ACTION_ID = "close"
ACTION_RULE = {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': 'closed'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Track action items and expected responses that arise from correspondence records.', 'actors': ['owner', 'office administrator'], 'primary_transitions': ['correspondence_followup: open -> in_progress -> closed -> archived']}

def handle_close(payload: dict, context: dict | None = None) -> dict:
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
