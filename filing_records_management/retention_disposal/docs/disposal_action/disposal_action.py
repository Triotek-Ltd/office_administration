"""Doc runtime hooks for disposal_action."""

class DocRuntime:
    doc_key = "disposal_action"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'submit', 'approve', 'close', 'archive']
