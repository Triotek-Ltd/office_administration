"""Doc runtime hooks for service_case."""

class DocRuntime:
    doc_key = "service_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'track', 'confirm', 'close', 'classify', 'escalate', 'record', 'archive']
