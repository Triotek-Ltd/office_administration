"""Doc runtime hooks for retention_policy."""

class DocRuntime:
    doc_key = "retention_policy"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'archive']
