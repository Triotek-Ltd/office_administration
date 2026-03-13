"""Doc runtime hooks for calendar_event."""

class DocRuntime:
    doc_key = "calendar_event"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'confirm', 'cancel', 'archive']
