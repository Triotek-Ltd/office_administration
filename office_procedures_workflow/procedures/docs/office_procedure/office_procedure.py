"""Doc runtime hooks for office_procedure."""

class DocRuntime:
    doc_key = "office_procedure"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'publish', 'archive']
