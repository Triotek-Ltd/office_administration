"""Action handler seed for correspondence_record:review."""

from __future__ import annotations


DOC_ID = "correspondence_record"
ACTION_ID = "review"
ACTION_RULE = {'allowed_in_states': ['draft', 'in_review', 'approved', 'sent'], 'transitions_to': 'in_review'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'receive, classify, assign, resolve, and document inquiries and complaints', 'actors': ['service desk officer', 'assigned department owner', 'supervisor', 'customer'], 'start_condition': 'a customer inquiry or complaint is received', 'ordered_steps': ['Confirm resolution with the customer.'], 'primary_actions': ['confirm', 'close'], 'primary_transitions': [], 'downstream_effects': ['service cases feed reporting, quality improvement, and risk/compliance review'], 'action_actors': {'create': ['service desk officer'], 'review': ['assigned department owner'], 'submit': ['service desk officer'], 'approve': ['supervisor'], 'issue': ['assigned department owner'], 'track': ['service desk officer'], 'archive': ['assigned department owner']}}

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
