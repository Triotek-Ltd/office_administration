"""Doc runtime hooks for document_access_request."""

class DocRuntime:
    doc_key = "document_access_request"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'approve', 'close']
