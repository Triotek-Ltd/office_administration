"""Doc runtime hooks for communication_log_entry."""

class DocRuntime:
    doc_key = "communication_log_entry"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'view', 'archive']
