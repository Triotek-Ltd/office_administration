"""Doc runtime hooks for meeting_record."""

class DocRuntime:
    doc_key = "meeting_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'confirm', 'close', 'archive']
