"""Workflow service seed for service_case."""

from __future__ import annotations


DOC_ID = "service_case"
ARCHETYPE = "workflow_case"
INITIAL_STATE = 'opened'
STATES = ['opened', 'in_progress', 'resolved', 'closed', 'archived']
TERMINAL_STATES = ['closed', 'archived']
ACTION_RULES = {'create': {'allowed_in_states': ['opened', 'in_progress', 'resolved'], 'transitions_to': None}, 'classify': {'allowed_in_states': ['opened', 'in_progress', 'resolved'], 'transitions_to': None}, 'escalate': {'allowed_in_states': ['opened', 'in_progress', 'resolved'], 'transitions_to': None}, 'track': {'allowed_in_states': ['opened', 'in_progress', 'resolved'], 'transitions_to': None}, 'assign': {'allowed_in_states': ['opened', 'in_progress', 'resolved'], 'transitions_to': 'in_progress'}, 'close': {'allowed_in_states': ['opened', 'in_progress', 'resolved'], 'transitions_to': 'closed'}, 'archive': {'allowed_in_states': ['opened', 'in_progress', 'resolved'], 'transitions_to': 'archived'}, 'confirm': {'allowed_in_states': ['opened', 'in_progress', 'resolved'], 'transitions_to': 'closed'}, 'record': {'allowed_in_states': ['opened', 'in_progress', 'resolved'], 'transitions_to': None}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'Receive, classify, assign, resolve, and document inquiries and complaints.', 'actors': ['service desk officer', 'assigned department owner', 'supervisor', 'customer'], 'start_condition': 'A customer inquiry or complaint is received.', 'ordered_steps': ['Open the service case and capture the issue.', 'Classify urgency and route to the responsible owner.', 'Record actions taken during handling.', 'Follow up unresolved issues.', 'Confirm resolution with the customer.'], 'primary_actions': ['create', 'assign', 'classify', 'escalate', 'confirm', 'close'], 'primary_transitions': ['service_case: opened -> in_progress', 'service_case: in_progress -> resolved -> closed'], 'downstream_effects': ['Service activity becomes auditable through log entries.', 'Follow-up actions can be assigned and tracked.', 'Resolution communication can be recorded.']}

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
        return rule.get("transitions_to")

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
