"""Action handler seed for travel_arrangement:create."""

from __future__ import annotations


DOC_ID = "travel_arrangement"
ACTION_ID = "create"
ACTION_RULE = {'allowed_in_states': ['draft', 'confirmed', 'cancelled'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Track travel plans linked to office events and participants.', 'actors': ['traveler', 'scheduler', 'office administrator'], 'primary_transitions': ['travel_arrangement: draft -> confirmed -> archived', 'travel_arrangement: draft -> cancelled']}

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
