"""Action handler seed for schedule_request:close."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "schedule_request"
ACTION_ID = "close"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['draft', 'proposed', 'confirmed', 'cancelled'], 'transitions_to': 'closed'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'receive scheduling requests, reserve time and resources, and manage related meeting or travel arrangements', 'actors': ['scheduler', 'participants', 'admin support'], 'start_condition': 'a meeting, travel, or calendar request is received', 'ordered_steps': ['Capture the scheduling or travel request.', 'Update the event for changes, conflicts, or cancellations.'], 'primary_actions': ['create', 'review', 'reschedule', 'cancel', 'close'], 'primary_transitions': ['schedule_request: draft -> in_review', 'schedule_request: in_review -> resolved -> closed'], 'downstream_effects': ['supports meetings, travel, and service coordination'], 'action_actors': {'create': ['scheduler'], 'review': ['participants'], 'confirm': ['participants'], 'cancel': ['scheduler'], 'close': ['scheduler']}}

def handle_close(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = cast(str | None, ACTION_RULE.get("transitions_to"))
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
