"""Action handler seed for schedule_request:review."""

from __future__ import annotations


DOC_ID = "schedule_request"
ACTION_ID = "review"
ACTION_RULE = {'allowed_in_states': ['draft', 'proposed', 'confirmed', 'cancelled'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Capture and progress scheduling requests into confirmed calendar events.', 'actors': ['requester', 'scheduler', 'office administrator'], 'primary_transitions': ['schedule_request: draft -> proposed -> confirmed -> closed', 'schedule_request: proposed -> cancelled']}

def handle_review(payload: dict, context: dict | None = None) -> dict:
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
