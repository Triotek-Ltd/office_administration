"""Action handler seed for correspondence_followup:close."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "correspondence_followup"
ACTION_ID = "close"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['open', 'in_progress'], 'transitions_to': 'closed'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['correspondence_record'], 'borrowed_fields': ['recipient', 'subject', 'communication date from correspondence_record'], 'inferred_roles': ['approver']}, 'actors': ['approver'], 'action_actors': {'create': ['approver'], 'assign': ['approver'], 'track': ['approver'], 'close': ['approver'], 'archive': ['approver']}}

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
