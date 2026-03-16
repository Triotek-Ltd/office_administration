"""Action handler seed for service_log_entry:archive."""

from __future__ import annotations


DOC_ID = "service_log_entry"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['active'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'receive, classify, assign, resolve, and document inquiries and complaints', 'actors': ['service desk officer', 'assigned department owner', 'supervisor', 'customer'], 'start_condition': 'a customer inquiry or complaint is received', 'ordered_steps': ['Record actions taken during handling.', 'Archive service documentation.'], 'primary_actions': ['record', 'view', 'archive'], 'primary_transitions': ['service_log_entry: active'], 'downstream_effects': ['service cases feed reporting, quality improvement, and risk/compliance review'], 'action_actors': {'record': ['service desk officer'], 'archive': ['assigned department owner']}}

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
