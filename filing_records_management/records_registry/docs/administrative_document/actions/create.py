"""Action handler seed for administrative_document:create."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "administrative_document"
ACTION_ID = "create"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['draft', 'active', 'disposed'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'register, store, retrieve, control, and dispose of administrative records', 'actors': ['records officer', 'document owner', 'requester', 'approver', 'archive custodian'], 'start_condition': 'a document is received or created and must be governed as a business record', 'ordered_steps': ['Intake and classify the document.', 'Assign internal reference and register the record.', 'Link retention and storage controls.', 'Store the record and make it retrievable.', 'Move inactive records toward archive handling.', 'Execute disposal when retention expires and approval exists.'], 'primary_actions': ['create', 'classify', 'register', 'record', 'review', 'update', 'archive', 'submit', 'approve', 'close'], 'primary_transitions': ['administrative_document: draft -> active', 'administrative_document: active -> archived -> disposed'], 'downstream_effects': ['records become available to compliance, audit, and legal processes', 'access and disposal events become auditable'], 'action_actors': {'create': ['records officer'], 'update': ['records officer'], 'review': ['document owner'], 'archive': ['document owner']}}

def handle_create(payload: dict, context: dict | None = None) -> dict:
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
