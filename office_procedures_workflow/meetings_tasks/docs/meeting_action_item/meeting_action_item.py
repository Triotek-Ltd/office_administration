"""Doc runtime hooks for meeting_action_item."""

class DocRuntime:
    doc_key = "meeting_action_item"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'track', 'close']
