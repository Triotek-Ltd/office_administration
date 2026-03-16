"""Action handler seed for travel_arrangement:issue."""

from __future__ import annotations


DOC_ID = "travel_arrangement"
ACTION_ID = "issue"
ACTION_RULE = {'allowed_in_states': ['draft', 'confirmed', 'cancelled'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'receive scheduling requests, reserve time and resources, and manage related meeting or travel arrangements', 'actors': ['scheduler', 'participants', 'admin support'], 'start_condition': 'a meeting, travel, or calendar request is received', 'ordered_steps': ['Create supporting travel arrangements where required.'], 'primary_actions': ['create', 'approve', 'issue', 'close'], 'primary_transitions': ['travel_arrangement: draft -> approved -> issued -> closed'], 'downstream_effects': ['supports meetings, travel, and service coordination'], 'action_actors': {'create': ['scheduler'], 'issue': ['admin support'], 'confirm': ['participants'], 'cancel': ['scheduler'], 'archive': ['scheduler']}}

def handle_issue(payload: dict, context: dict | None = None) -> dict:
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
