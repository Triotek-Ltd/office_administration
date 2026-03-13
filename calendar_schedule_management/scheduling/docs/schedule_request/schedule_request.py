"""Doc runtime hooks for schedule_request."""

class DocRuntime:
    doc_key = "schedule_request"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'confirm', 'cancel', 'close']
