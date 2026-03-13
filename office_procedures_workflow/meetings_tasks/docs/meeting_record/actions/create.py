"""Action handler seed for meeting_record:create."""

from __future__ import annotations


DOC_ID = "meeting_record"
ACTION_ID = "create"
ACTION_RULE = {'allowed_in_states': ['draft', 'scheduled', 'completed'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Capture the schedule, agenda, attendance, and outcomes of office meetings.', 'actors': ['chair', 'recorder', 'office administrator'], 'primary_transitions': ['meeting_record: draft -> scheduled -> completed -> archived']}

def handle_create(payload: dict, context: dict | None = None) -> dict:
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
