"""Doc runtime hooks for records_register_entry."""

class DocRuntime:
    doc_key = "records_register_entry"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'record', 'review', 'archive', 'view']
