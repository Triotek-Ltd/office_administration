"""Doc runtime hooks for tool_issue_case."""

class DocRuntime:
    doc_key = "tool_issue_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'escalate', 'close', 'archive']
