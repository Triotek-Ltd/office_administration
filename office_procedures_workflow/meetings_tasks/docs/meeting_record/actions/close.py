"""Action handler seed for meeting_record:close."""

from __future__ import annotations


DOC_ID = "meeting_record"
ACTION_ID = "close"
ACTION_RULE = {'allowed_in_states': ['draft', 'scheduled', 'completed'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'receive scheduling requests, reserve time and resources, and manage related meeting or travel arrangements', 'actors': ['scheduler', 'participants', 'admin support'], 'start_condition': 'a meeting, travel, or calendar request is received', 'ordered_steps': [], 'primary_actions': [], 'primary_transitions': [], 'downstream_effects': ['supports meetings, travel, and service coordination'], 'action_actors': {'create': ['scheduler'], 'update': ['scheduler'], 'confirm': ['participants'], 'close': ['scheduler'], 'archive': ['scheduler']}}

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
