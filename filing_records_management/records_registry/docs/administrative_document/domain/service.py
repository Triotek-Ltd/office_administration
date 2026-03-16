"""Business-domain service seed for Administrative Document."""

from __future__ import annotations


ARCHETYPE_PROFILE = {'workflow_profile': {'mode': 'entity_lifecycle', 'case_management': False}, 'reporting_profile': {'supports_snapshots': False, 'supports_outputs': False}, 'integration_profile': {'external_sync_enabled': False}, 'lifecycle_states': ['draft', 'active', 'archived', 'disposed'], 'is_transactional': False}

CONTRACT = {'title_field': 'title', 'status_field': 'workflow_state', 'reference_field': 'reference_no', 'required_fields': ['title', 'workflow_state'], 'field_purposes': {'workflow_state': 'lifecycle_state', 'document_date': 'schedule_marker', 'related_records_register_entry': 'relation_collection', 'related_document_access_request': 'relation_collection', 'related_disposal_action': 'relation_collection'}, 'search_fields': ['title', 'reference_no', 'description', 'reference_number', 'classification', 'record_type'], 'list_columns': ['title', 'reference_no', 'workflow_state', 'modified'], 'initial_state': 'draft', 'lifecycle_states': ['draft', 'active', 'archived', 'disposed'], 'terminal_states': ['archived'], 'action_targets': {'create': None, 'update': None, 'review': None, 'archive': 'archived', 'classify': None, 'file': None, 'register': None}}

WORKFLOW_HINTS = {'business_objective': 'register, store, retrieve, control, and dispose of administrative records', 'actors': ['records officer', 'document owner', 'requester', 'approver', 'archive custodian'], 'start_condition': 'a document is received or created and must be governed as a business record', 'ordered_steps': ['Intake and classify the document.', 'Assign internal reference and register the record.', 'Link retention and storage controls.', 'Store the record and make it retrievable.', 'Move inactive records toward archive handling.', 'Execute disposal when retention expires and approval exists.'], 'primary_actions': ['create', 'classify', 'register', 'record', 'review', 'update', 'archive', 'submit', 'approve', 'close'], 'primary_transitions': ['administrative_document: draft -> active', 'administrative_document: active -> archived -> disposed'], 'downstream_effects': ['records become available to compliance, audit, and legal processes', 'access and disposal events become auditable'], 'action_actors': {'create': ['records officer'], 'update': ['records officer'], 'review': ['document owner'], 'archive': ['document owner']}}

SIDE_EFFECT_HINTS = {'downstream_effects': ['records become available to compliance, audit, and legal processes', 'access and disposal events become auditable'], 'related_docs': ['document_classification', 'retention_policy', 'records_register_entry', 'document_access_request', 'disposal_action'], 'action_targets': {'create': None, 'update': None, 'review': None, 'archive': 'archived', 'classify': None, 'file': None, 'register': None}, 'action_side_effects_file': 'side_effects.json'}

class DomainService:
    doc_id = "administrative_document"
    archetype = "master"
    doc_kind = "master"

    def required_fields(self) -> list[str]:
        return CONTRACT.get("required_fields", [])

    def state_field(self) -> str | None:
        return CONTRACT.get("status_field")

    def default_state(self) -> str | None:
        return CONTRACT.get("initial_state")

    def list_columns(self) -> list[str]:
        return CONTRACT.get("list_columns", [])

    def validate_invariants(self, payload: dict, *, partial: bool = False) -> dict:
        if partial:
            required_scope = [field for field in self.required_fields() if field in payload]
        else:
            required_scope = self.required_fields()
        missing_fields = [field for field in required_scope if not payload.get(field)]
        if missing_fields:
            raise ValueError(f"Missing required business fields: {', '.join(missing_fields)}")
        state_field = self.state_field()
        allowed_states = set(CONTRACT.get("lifecycle_states", []))
        if state_field and payload.get(state_field) and allowed_states and payload[state_field] not in allowed_states:
            raise ValueError(f"Invalid state '{payload[state_field]}' for {state_field}")
        return payload

    def prepare_create_payload(self, payload: dict, context: dict | None = None) -> dict:
        payload = dict(payload)
        state_field = self.state_field()
        if state_field and not payload.get(state_field) and self.default_state():
            payload[state_field] = self.default_state()
        title_field = CONTRACT.get("title_field")
        reference_field = CONTRACT.get("reference_field")
        if title_field and not payload.get(title_field) and reference_field and payload.get(reference_field):
            payload[title_field] = str(payload[reference_field])
        payload = self.validate_invariants(payload)
        return payload

    def after_create(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        return serialized_data

    def prepare_update_payload(self, instance, payload: dict, context: dict | None = None) -> dict:
        payload = dict(payload)
        payload = self.validate_invariants(payload, partial=True)
        return payload

    def after_update(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        return serialized_data

    def after_action(
        self,
        instance,
        action_id: str,
        payload: dict,
        action_result: dict,
        context: dict | None = None,
    ) -> dict:
        return {
            "updates": {},
            "side_effects": [],
        }

    def shape_retrieve_data(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        serialized_data.setdefault("_business_capabilities", self.business_capabilities())
        return serialized_data

    def workflow_objective(self) -> str | None:
        return WORKFLOW_HINTS.get("business_objective")

    def side_effect_hints(self) -> dict:
        return SIDE_EFFECT_HINTS

    def business_capabilities(self) -> dict:
        return {
            **ARCHETYPE_PROFILE,
            "required_fields": self.required_fields(),
            "state_field": self.state_field(),
            "default_state": self.default_state(),
        }
