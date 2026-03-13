"""Doc runtime hooks for participant."""

class DocRuntime:
    doc_key = "participant"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'archive']
