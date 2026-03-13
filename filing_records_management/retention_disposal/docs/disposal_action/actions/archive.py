"""Action handler seed for disposal_action:archive."""

from __future__ import annotations


DOC_ID = "disposal_action"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['draft', 'in_review', 'approved'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Track approval and completion of records disposal under retention controls.', 'actors': ['records officer', 'approver', 'custodian'], 'primary_transitions': ['disposal_action: draft -> in_review -> approved -> closed -> archived']}

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
