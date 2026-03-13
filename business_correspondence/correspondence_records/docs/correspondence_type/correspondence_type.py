"""Doc runtime hooks for correspondence_type."""

class DocRuntime:
    doc_key = "correspondence_type"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'archive']
