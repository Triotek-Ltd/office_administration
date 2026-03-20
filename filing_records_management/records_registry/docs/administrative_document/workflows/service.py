"""Workflow service seed for administrative_document."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "administrative_document"
ARCHETYPE = "master"
INITIAL_STATE = 'draft'
STATES = ['draft', 'active', 'archived', 'disposed']
TERMINAL_STATES = ['archived']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['draft', 'active', 'disposed'], 'transitions_to': None}, 'update': {'allowed_in_states': ['draft', 'active', 'disposed'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'active', 'disposed'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'active', 'disposed'], 'transitions_to': 'archived'}, 'classify': {'allowed_in_states': ['draft', 'active', 'disposed'], 'transitions_to': None}, 'file': {'allowed_in_states': ['draft', 'active', 'disposed'], 'transitions_to': None}, 'register': {'allowed_in_states': ['draft', 'active', 'disposed'], 'transitions_to': None}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'register, store, retrieve, control, and dispose of administrative records', 'actors': ['records officer', 'document owner', 'requester', 'approver', 'archive custodian'], 'start_condition': 'a document is received or created and must be governed as a business record', 'ordered_steps': ['Intake and classify the document.', 'Assign internal reference and register the record.', 'Link retention and storage controls.', 'Store the record and make it retrievable.', 'Move inactive records toward archive handling.', 'Execute disposal when retention expires and approval exists.'], 'primary_actions': ['create', 'classify', 'register', 'record', 'review', 'update', 'archive', 'submit', 'approve', 'close'], 'primary_transitions': ['administrative_document: draft -> active', 'administrative_document: active -> archived -> disposed'], 'downstream_effects': ['records become available to compliance, audit, and legal processes', 'access and disposal events become auditable'], 'action_actors': {'create': ['records officer'], 'update': ['records officer'], 'review': ['document owner'], 'archive': ['document owner']}}

class WorkflowService:
    def allowed_actions_for_state(self, state: str | None) -> list[str]:
        if not state:
            return list(ACTION_RULES.keys())
        allowed = []
        for action_id, rule in ACTION_RULES.items():
            states = rule.get("allowed_in_states") or []
            if not states or state in states:
                allowed.append(action_id)
        return allowed

    def is_action_allowed(self, action_id: str, state: str | None) -> bool:
        return action_id in self.allowed_actions_for_state(state)

    def next_state_for(self, action_id: str) -> str | None:
        rule = ACTION_RULES.get(action_id, {})
        return cast(str | None, rule.get("transitions_to"))

    def apply_action(self, action_id: str, state: str | None) -> dict:
        if not self.is_action_allowed(action_id, state):
            raise ValueError(f"Action '{action_id}' is not allowed in state '{state}'")
        next_state = self.next_state_for(action_id)
        updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
        return {
            "action_id": action_id,
            "current_state": state,
            "next_state": next_state,
            "updates": updates,
        }

    def is_terminal(self, state: str | None) -> bool:
        return bool(state and state in TERMINAL_STATES)

    def workflow_summary(self) -> dict:
        return {
            "initial_state": INITIAL_STATE,
            "states": STATES,
            "terminal_states": TERMINAL_STATES,
            "business_objective": WORKFLOW_HINTS.get("business_objective"),
            "ordered_steps": WORKFLOW_HINTS.get("ordered_steps", []),
        }

    def workflow_profile(self) -> dict:
        return {'mode': 'entity_lifecycle', 'case_management': False}
