"""Action handler seed for office_file_record:review."""

from __future__ import annotations


DOC_ID = "office_file_record"
ACTION_ID = "review"
ACTION_RULE = {'allowed_in_states': ['draft', 'active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'govern office files and tool access, and resolve day-to-day office-system support issues', 'actors': ['office user', 'system admin', 'support owner'], 'start_condition': 'an office document or tool access/update event occurs', 'ordered_steps': ['Register or update the office file record.'], 'primary_actions': ['create', 'update', 'archive'], 'primary_transitions': ['office_file_record: draft -> active'], 'downstream_effects': ['supports office controls and operational continuity'], 'action_actors': {'create': ['office user'], 'update': ['office user'], 'review': ['system admin'], 'archive': ['support owner']}}

def handle_review(payload: dict, context: dict | None = None) -> dict:
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
