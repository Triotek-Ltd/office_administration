"""Doc runtime hooks for correspondence_approval."""

class DocRuntime:
    doc_key = "correspondence_approval"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['submit', 'approve', 'return_for_revision', 'close']
