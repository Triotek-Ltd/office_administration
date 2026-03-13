"""Doc runtime hooks for customer_profile."""

class DocRuntime:
    doc_key = "customer_profile"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'view', 'archive']
