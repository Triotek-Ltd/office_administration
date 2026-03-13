"""Doc runtime hooks for version_record."""

class DocRuntime:
    doc_key = "version_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'view', 'archive']
