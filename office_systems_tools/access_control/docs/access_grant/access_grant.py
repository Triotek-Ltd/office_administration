"""Doc runtime hooks for access_grant."""

class DocRuntime:
    doc_key = "access_grant"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'approve', 'close', 'archive']
