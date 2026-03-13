"""Action handler seed for document_classification:archive."""

from __future__ import annotations


DOC_ID = "document_classification"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': 'active', 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Define the classification scheme used to organize and secure administrative documents.', 'actors': ['records officer'], 'primary_transitions': ['document_classification: active -> archived']}

def handle_archive(payload: dict, context: dict | None = None) -> dict:
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
