"""Action handler seed for disposal_action:create."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "disposal_action"
ACTION_ID = "create"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['draft', 'in_review', 'approved'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'register, store, retrieve, control, and dispose of administrative records', 'actors': ['records officer', 'document owner', 'requester', 'approver', 'archive custodian'], 'start_condition': 'a document is received or created and must be governed as a business record', 'ordered_steps': ['Execute disposal when retention expires and approval exists.'], 'primary_actions': ['create', 'submit', 'approve', 'close', 'archive'], 'primary_transitions': ['disposal_action: draft -> in_review -> approved -> closed -> archived'], 'downstream_effects': ['records become available to compliance, audit, and legal processes', 'access and disposal events become auditable'], 'action_actors': {'create': ['records officer'], 'submit': ['records officer'], 'approve': ['approver'], 'close': ['document owner'], 'archive': ['document owner']}}

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
