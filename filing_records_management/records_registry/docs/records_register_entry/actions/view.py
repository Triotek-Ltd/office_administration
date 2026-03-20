"""Action handler seed for records_register_entry:view."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "records_register_entry"
ACTION_ID = "view"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['draft', 'active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'draft, approve, send, record, and follow up formal business communications', 'actors': ['administrative officer', 'drafter', 'approver', 'recipient', 'follow-up owner'], 'start_condition': 'incoming communication is received or outgoing correspondence must be initiated', 'ordered_steps': ['File the communication into the records system.'], 'primary_actions': ['register', 'record', 'archive'], 'primary_transitions': [], 'downstream_effects': ['correspondence becomes available to records, audit, legal, and service workflows'], 'action_actors': {'create': ['administrative officer'], 'record': ['administrative officer'], 'review': ['drafter'], 'archive': ['follow-up owner']}}

def handle_view(payload: dict, context: dict | None = None) -> dict:
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
