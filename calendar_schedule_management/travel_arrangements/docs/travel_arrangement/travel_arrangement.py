"""Doc runtime hooks for travel_arrangement."""

class DocRuntime:
    doc_key = "travel_arrangement"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'issue', 'confirm', 'cancel', 'archive']
