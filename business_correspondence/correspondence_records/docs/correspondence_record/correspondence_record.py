"""Doc runtime hooks for correspondence_record."""

class DocRuntime:
    doc_key = "correspondence_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'submit', 'approve', 'return_for_revision', 'issue', 'send', 'file', 'track', 'archive']
