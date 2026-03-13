"""Action handler seed for workflow_task:track."""

from __future__ import annotations


DOC_ID = "workflow_task"
ACTION_ID = "track"
ACTION_RULE = {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Track office work items created from procedures, meetings, and follow-through requirements.', 'actors': ['assignee', 'owner', 'office administrator'], 'primary_transitions': ['workflow_task: open -> in_progress -> closed -> archived']}

def handle_track(payload: dict, context: dict | None = None) -> dict:
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
