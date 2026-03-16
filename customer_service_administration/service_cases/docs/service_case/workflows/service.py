"""Workflow service seed for service_case."""

from __future__ import annotations


DOC_ID = "service_case"
ARCHETYPE = "workflow_case"
INITIAL_STATE = 'open'
STATES = ['open', 'in_progress', 'resolved', 'closed', 'archived']
TERMINAL_STATES = ['closed', 'archived']
ACTION_RULES = {'create': {'allowed_in_states': ['open', 'in_progress', 'resolved'], 'transitions_to': None}, 'assign': {'allowed_in_states': ['open', 'in_progress', 'resolved'], 'transitions_to': 'in_progress'}, 'track': {'allowed_in_states': ['open', 'in_progress', 'resolved'], 'transitions_to': None}, 'confirm': {'allowed_in_states': ['open', 'in_progress', 'resolved'], 'transitions_to': 'closed'}, 'close': {'allowed_in_states': ['open', 'in_progress', 'resolved'], 'transitions_to': 'closed'}, 'classify': {'allowed_in_states': ['open', 'in_progress', 'resolved'], 'transitions_to': None}, 'escalate': {'allowed_in_states': ['open', 'in_progress', 'resolved'], 'transitions_to': None}, 'record': {'allowed_in_states': ['open', 'in_progress', 'resolved'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['open', 'in_progress', 'resolved'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'receive, classify, assign, resolve, and document inquiries and complaints', 'actors': ['service desk officer', 'assigned department owner', 'supervisor', 'customer'], 'start_condition': 'a customer inquiry or complaint is received', 'ordered_steps': ['Open the service case and capture the issue.', 'Classify urgency and route to the responsible owner.', 'Follow up unresolved issues.', 'Confirm resolution with the customer.', 'Archive service documentation.'], 'primary_actions': ['create', 'assign', 'classify', 'escalate', 'track', 'confirm', 'close', 'archive'], 'primary_transitions': ['service_case: opened -> in_progress', 'service_case: in_progress -> resolved -> closed'], 'downstream_effects': ['service cases feed reporting, quality improvement, and risk/compliance review'], 'action_actors': {'create': ['service desk officer'], 'assign': ['service desk officer'], 'track': ['service desk officer'], 'confirm': ['supervisor'], 'close': ['assigned department owner'], 'record': ['service desk officer'], 'archive': ['assigned department owner']}}

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
