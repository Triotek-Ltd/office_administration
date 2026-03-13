"""Action handler seed for administrative_document:classify."""

from __future__ import annotations


DOC_ID = "administrative_document"
ACTION_ID = "classify"
ACTION_RULE = {'allowed_in_states': ['draft', 'active', 'disposed'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Register, classify, file, and retain internal administrative documents under office records controls.', 'actors': ['records officer', 'office administrator', 'custodian'], 'primary_transitions': ['administrative_document: draft -> active -> archived -> disposed']}

def handle_classify(payload: dict, context: dict | None = None) -> dict:
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
