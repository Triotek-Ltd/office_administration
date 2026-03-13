"""Action handler seed for calendar_event:confirm."""

from __future__ import annotations


DOC_ID = "calendar_event"
ACTION_ID = "confirm"
ACTION_RULE = {'allowed_in_states': ['scheduled', 'completed', 'cancelled'], 'transitions_to': 'completed'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Maintain scheduled office events and their participant context.', 'actors': ['organizer', 'scheduler', 'office administrator'], 'primary_transitions': ['calendar_event: scheduled -> completed -> archived', 'calendar_event: scheduled -> cancelled']}

def handle_confirm(payload: dict, context: dict | None = None) -> dict:
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
