"""Action handler seed for calendar_event:update."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "calendar_event"
ACTION_ID = "update"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['scheduled', 'completed', 'cancelled'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'receive scheduling requests, reserve time and resources, and manage related meeting or travel arrangements', 'actors': ['scheduler', 'participants', 'admin support'], 'start_condition': 'a meeting, travel, or calendar request is received', 'ordered_steps': ['Confirm availability and reserve the calendar slot.', 'Update the event for changes, conflicts, or cancellations.'], 'primary_actions': ['create', 'schedule', 'confirm', 'reschedule', 'cancel', 'close'], 'primary_transitions': ['calendar_event: draft -> scheduled -> confirmed', 'calendar_event: confirmed -> rescheduled or cancelled -> closed'], 'downstream_effects': ['supports meetings, travel, and service coordination'], 'action_actors': {'create': ['scheduler'], 'update': ['scheduler'], 'confirm': ['participants'], 'cancel': ['scheduler'], 'archive': ['scheduler']}}

def handle_update(payload: dict, context: dict | None = None) -> dict:
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
