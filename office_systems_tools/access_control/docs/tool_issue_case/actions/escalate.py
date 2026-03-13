"""Action handler seed for tool_issue_case:escalate."""

from __future__ import annotations


DOC_ID = "tool_issue_case"
ACTION_ID = "escalate"
ACTION_RULE = {'allowed_in_states': ['open', 'in_progress', 'escalated'], 'transitions_to': 'escalated'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Track support and incident-style issues against office tools and managed systems.', 'actors': ['reporter', 'support owner', 'office administrator'], 'primary_transitions': ['tool_issue_case: open -> in_progress -> escalated or closed -> archived']}

def handle_escalate(payload: dict, context: dict | None = None) -> dict:
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
