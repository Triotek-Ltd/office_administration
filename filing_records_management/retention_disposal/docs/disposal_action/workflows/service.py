"""Workflow service seed for disposal_action."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "disposal_action"
ARCHETYPE = "workflow_case"
INITIAL_STATE = 'draft'
STATES = ['draft', 'in_review', 'approved', 'closed', 'archived']
TERMINAL_STATES = ['closed', 'archived']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['draft', 'in_review', 'approved'], 'transitions_to': None}, 'submit': {'allowed_in_states': ['draft', 'in_review', 'approved'], 'transitions_to': 'in_review'}, 'approve': {'allowed_in_states': ['draft', 'in_review', 'approved'], 'transitions_to': 'approved'}, 'close': {'allowed_in_states': ['draft', 'in_review', 'approved'], 'transitions_to': 'closed'}, 'archive': {'allowed_in_states': ['draft', 'in_review', 'approved'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'register, store, retrieve, control, and dispose of administrative records', 'actors': ['records officer', 'document owner', 'requester', 'approver', 'archive custodian'], 'start_condition': 'a document is received or created and must be governed as a business record', 'ordered_steps': ['Execute disposal when retention expires and approval exists.'], 'primary_actions': ['create', 'submit', 'approve', 'close', 'archive'], 'primary_transitions': ['disposal_action: draft -> in_review -> approved -> closed -> archived'], 'downstream_effects': ['records become available to compliance, audit, and legal processes', 'access and disposal events become auditable'], 'action_actors': {'create': ['records officer'], 'submit': ['records officer'], 'approve': ['approver'], 'close': ['document owner'], 'archive': ['document owner']}}

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
        return {'mode': 'case_flow', 'supports_assignment': True, 'supports_escalation': True}
