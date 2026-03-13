"""Doc runtime hooks for document_classification."""

class DocRuntime:
    doc_key = "document_classification"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'archive']
