"""Action handler seed for service_resolution:archive."""

from __future__ import annotations


DOC_ID = "service_resolution"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['draft', 'confirmed'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Capture and confirm the final service outcome for a customer case.', 'actors': ['assigned owner', 'service supervisor', 'customer'], 'start_condition': 'A service case has reached a proposed outcome that requires confirmation.', 'ordered_steps': ['Create the service resolution record from the case context.', 'Review the proposed outcome.', 'Confirm the resolution with the relevant party.', 'Archive the final resolution record.'], 'primary_actions': ['create', 'review', 'confirm', 'archive'], 'primary_transitions': ['service_resolution: draft -> confirmed -> archived'], 'downstream_effects': ['Resolved case outcomes become traceable and reviewable.']}

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
