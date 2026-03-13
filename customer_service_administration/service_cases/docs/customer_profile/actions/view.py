"""Action handler seed for customer_profile:view."""

from __future__ import annotations


DOC_ID = "customer_profile"
ACTION_ID = "view"
ACTION_RULE = {'allowed_in_states': 'active', 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Maintain the service-facing customer identity and contact context used across service cases.', 'actors': ['service desk officer', 'customer service supervisor'], 'start_condition': 'A service interaction requires a customer-facing party record.', 'ordered_steps': ['Create or update the customer profile.', 'Record contact details and preferred communication method.', 'Use the profile to support service-case handling.'], 'primary_actions': ['create', 'update', 'view', 'archive'], 'primary_transitions': ['customer_profile: active -> archived'], 'downstream_effects': ['Service cases can reuse customer identity and contact details.']}

def handle_view(payload: dict, context: dict | None = None) -> dict:
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
