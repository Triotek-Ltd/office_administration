"""Action handler seed for office_procedure:publish."""

from __future__ import annotations


DOC_ID = "office_procedure"
ACTION_ID = "publish"
ACTION_RULE = {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': 'published'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'maintain standard office procedures, run recurring coordination meetings, and ensure agreed actions are tracked to closure', 'actors': ['admin coordinator', 'meeting owner', 'task owners'], 'start_condition': 'an internal procedure or meeting-driven workflow must be coordinated', 'ordered_steps': ['Create or revise the office procedure baseline.'], 'primary_actions': ['create', 'update', 'review', 'approve'], 'primary_transitions': ['office_procedure: draft -> in_review -> approved -> active'], 'downstream_effects': ['supports coordination, compliance, and operational follow-through'], 'action_actors': {'create': ['admin coordinator'], 'update': ['admin coordinator'], 'review': ['admin coordinator'], 'publish': ['meeting owner'], 'archive': ['meeting owner']}}

def handle_publish(payload: dict, context: dict | None = None) -> dict:
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
