"""Doc runtime hooks for service_resolution."""

class DocRuntime:
    doc_key = "service_resolution"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'confirm', 'archive']
