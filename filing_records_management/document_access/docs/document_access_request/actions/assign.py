"""Action handler seed for document_access_request:assign."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "document_access_request"
ACTION_ID = "assign"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['open', 'in_review', 'resolved'], 'transitions_to': 'in_review'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'register, store, retrieve, control, and dispose of administrative records', 'actors': ['records officer', 'document owner', 'requester', 'approver', 'archive custodian'], 'start_condition': 'a document is received or created and must be governed as a business record', 'ordered_steps': ['Handle retrieval and access requests.'], 'primary_actions': ['create', 'assign', 'approve', 'record', 'close'], 'primary_transitions': ['document_access_request: opened -> in_review -> resolved -> closed'], 'downstream_effects': ['records become available to compliance, audit, and legal processes', 'access and disposal events become auditable'], 'action_actors': {'create': ['records officer'], 'assign': ['records officer'], 'approve': ['approver'], 'close': ['document owner']}}

def handle_assign(payload: dict, context: dict | None = None) -> dict:
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
