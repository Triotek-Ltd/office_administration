"""Doc runtime hooks for correspondence_followup."""

class DocRuntime:
    doc_key = "correspondence_followup"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'track', 'close', 'archive']
