"""Doc runtime hooks for office_file_record."""

class DocRuntime:
    doc_key = "office_file_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'archive']
