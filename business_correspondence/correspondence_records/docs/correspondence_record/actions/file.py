"""Action handler seed for correspondence_record:file."""

from __future__ import annotations


DOC_ID = "correspondence_record"
ACTION_ID = "file"
ACTION_RULE = {'allowed_in_states': ['draft', 'in_review', 'approved', 'sent'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Prepare, route, approve, send, and file internal and external correspondence records.', 'actors': ['office administrator', 'approver', 'correspondence owner'], 'primary_transitions': ['correspondence_record: draft -> in_review -> approved -> sent -> archived']}

def handle_file(payload: dict, context: dict | None = None) -> dict:
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
