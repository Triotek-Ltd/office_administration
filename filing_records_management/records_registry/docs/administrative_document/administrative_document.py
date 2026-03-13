"""Doc runtime hooks for administrative_document."""

class DocRuntime:
    doc_key = "administrative_document"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'archive', 'classify', 'file', 'register']
