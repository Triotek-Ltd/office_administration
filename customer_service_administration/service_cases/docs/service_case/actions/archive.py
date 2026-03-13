"""Action handler seed for service_case:archive."""

from __future__ import annotations


DOC_ID = "service_case"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['opened', 'in_progress', 'resolved'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Receive, classify, assign, resolve, and document inquiries and complaints.', 'actors': ['service desk officer', 'assigned department owner', 'supervisor', 'customer'], 'start_condition': 'A customer inquiry or complaint is received.', 'ordered_steps': ['Open the service case and capture the issue.', 'Classify urgency and route to the responsible owner.', 'Record actions taken during handling.', 'Follow up unresolved issues.', 'Confirm resolution with the customer.'], 'primary_actions': ['create', 'assign', 'classify', 'escalate', 'confirm', 'close'], 'primary_transitions': ['service_case: opened -> in_progress', 'service_case: in_progress -> resolved -> closed'], 'downstream_effects': ['Service activity becomes auditable through log entries.', 'Follow-up actions can be assigned and tracked.', 'Resolution communication can be recorded.']}

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
