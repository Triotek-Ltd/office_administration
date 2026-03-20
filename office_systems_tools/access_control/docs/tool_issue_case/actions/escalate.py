"""Action handler seed for tool_issue_case:escalate."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "tool_issue_case"
ACTION_ID = "escalate"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['open', 'in_progress', 'escalated'], 'transitions_to': 'escalated'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['office_file_record'], 'borrowed_fields': ['system or file context from office_file_record'], 'inferred_roles': ['case owner']}, 'actors': ['case owner'], 'action_actors': {'create': ['case owner'], 'assign': ['case owner'], 'close': ['case owner'], 'archive': ['case owner']}}

def handle_escalate(payload: dict, context: dict | None = None) -> dict:
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
